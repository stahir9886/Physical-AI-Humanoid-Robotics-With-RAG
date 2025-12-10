from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from src.services.database import DatabaseService
from src.services.rag_service import RAGService
from src.middleware.rate_limit import RateLimitMiddleware
import os
import logging

# Configure logging
logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))
logger = logging.getLogger(__name__)

# Create global service instances
db_service = DatabaseService()
rag_service = RAGService()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler to manage app startup and shutdown."""
    # Startup
    logger.info("Initializing database connection...")
    await db_service.connect()
    logger.info("Database connection initialized.")

    logger.info("RAG service initialized.")

    yield  # App runs here

    # Shutdown
    logger.info("Closing database connection...")
    await db_service.disconnect()
    logger.info("Database connection closed.")


# Create FastAPI app
app = FastAPI(
    title="Textbook RAG API",
    description="API for the AI-Native Physical AI & Humanoid Robotics Textbook with RAG functionality",
    version="1.0.0",
    lifespan=lifespan,
    # In production, you might want to disable docs/swagger to reduce attack surface
    # docs_url=None, redoc_url=None  # Uncomment these in high-security environments
)

# Add rate limiting middleware first
app.add_middleware(RateLimitMiddleware)

# Configure CORS - in production, specify exact origins instead of "*"
allowed_origins = os.getenv("ALLOWED_ORIGINS", "").split(",")
if not allowed_origins or allowed_origins == [""]:
    # Default to all origins during development, but this should be restricted in production
    allowed_origins = ["*"]  # This should be changed in production

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # Allow specific headers if needed
    # expose_headers=["Access-Control-Allow-Origin"]
)

# Import and include routers after app creation to avoid circular imports
# These imports need to be here after middleware is added
from src.api.routes import chapters, chat, profile, personalization

app.include_router(chapters.router, prefix="/api", tags=["chapters"])
app.include_router(chat.router, prefix="/api", tags=["chat"])
app.include_router(profile.router, prefix="/api", tags=["profile"])
app.include_router(personalization.router, prefix="/api", tags=["personalization"])

@app.get("/")
def read_root():
    return {"message": "Textbook RAG API is running!"}

@app.get("/health")
def health_check():
    """Health check endpoint for deployment monitoring."""
    return {"status": "healthy", "message": "All services operational"}

@app.get("/ready")
def readiness_check():
    """Readiness check endpoint for deployment monitoring."""
    # In a real implementation, this might check database connectivity,
    # external service availability, etc.
    return {"status": "ready", "message": "Service ready to accept requests"}