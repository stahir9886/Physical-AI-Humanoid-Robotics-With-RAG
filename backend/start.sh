#!/bin/bash
# Production startup script for the textbook backend

# Run database migrations if needed
# python -m src.scripts.migrate

# Start the FastAPI application with uvicorn
exec uvicorn src.api.main:app --host 0.0.0.0 --port $PORT --workers 4