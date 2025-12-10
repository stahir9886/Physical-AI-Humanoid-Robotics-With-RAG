# AI-Native Physical AI & Humanoid Robotics Textbook

This project implements an interactive textbook with a RAG (Retrieval Augmented Generation) chatbot to help students learn about Physical AI and Humanoid Robotics.

## Architecture

The application consists of two main components:

1. **Frontend**: Docusaurus-based textbook interface, deployed to GitHub Pages
2. **Backend**: FastAPI-based RAG service, deployed to Railway/Render

## Deployment Instructions

### Frontend (Docusaurus to GitHub Pages)

The frontend is automatically deployed to GitHub Pages using GitHub Actions. The workflow is defined in `.github/workflows/deploy.yml`.

#### Manual Deployment Steps:
1. Ensure the `baseUrl` and `organizationName`/`projectName` in `docusaurus.config.ts` match your GitHub repository
2. The workflow automatically builds and deploys when you push to the `main` branch

#### GitHub Pages Configuration:
1. Go to your repository settings
2. Navigate to "Pages" section
3. Select source as "GitHub Actions"

### Backend (FastAPI to Railway/Render)

#### Railway Deployment:
1. Connect your GitHub repository to Railway
2. Railway will automatically detect the project and use the settings in `railway.toml`
3. Add the required environment variables:
   - `OPENAI_API_KEY`
   - `QDRANT_HOST`
   - `NEON_DATABASE_URL`
4. Deploy the application

#### Render Deployment:
1. Create a new Web Service on Render
2. Connect to your GitHub repository
3. Use the settings from `render.yaml`
4. Add the required environment variables:
   - `OPENAI_API_KEY`
   - `QDRANT_HOST`
   - `NEON_DATABASE_URL`
5. Deploy the application

### Environment Variables

#### Backend Required Variables:
- `OPENAI_API_KEY` - API key for OpenAI services
- `QDRANT_HOST` - Host address for Qdrant vector database
- `QDRANT_PORT` - Port for Qdrant (default: 6333)
- `NEON_DATABASE_URL` - Connection string for Neon Postgres database
- `RATE_LIMIT_REQUESTS` - Number of requests allowed in the rate limit window (default: 100)
- `RATE_LIMIT_WINDOW` - Time window in seconds for rate limiting (default: 3600)
- `ENVIRONMENT` - Environment type (default: production)
- `LOG_LEVEL` - Logging level (default: INFO)

## Health Checks

The application provides health check endpoints:
- `GET /health` - General health status
- `GET /ready` - Readiness for requests

Run the health check script to verify your deployment:
```bash
python health_check.py [your-api-url]
```

## Launch Checklist

Before going live, complete the items in `LAUNCH_CHECKLIST.md`.

## Directory Structure

```
Physical-AI-Humanoid-Robotics/
├── backend/                 # FastAPI backend
│   ├── src/
│   │   ├── api/            # API routes
│   │   ├── models/         # Data models
│   │   ├── services/       # Business logic
│   │   ├── middleware/     # Request processing
│   │   └── utils/          # Utilities
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Container configuration
│   └── start.sh            # Startup script
├── docusaurus/             # Docusaurus frontend
│   ├── docs/               # Textbook content
│   ├── src/                # Custom components
│   ├── static/             # Static assets
│   └── docusaurus.config.ts # Site configuration
├── .github/workflows/      # GitHub Actions workflows
├── railway.toml            # Railway deployment config
├── render.yaml             # Render deployment config
├── LAUNCH_CHECKLIST.md     # Pre-launch checklist
└── health_check.py         # Health verification script
```

## Technology Stack

- **Frontend**: Docusaurus (React-based static site generator)
- **Backend**: FastAPI (Python web framework)
- **Database**: Neon Postgres (PostgreSQL-compatible serverless database)
- **Vector Database**: Qdrant (vector similarity search engine)
- **Language Model**: OpenAI API
- **Hosting (Backend)**: Railway or Render
- **Hosting (Frontend)**: GitHub Pages
- **Documentation**: Markdown content with Docusaurus
- **API Documentation**: Automatic OpenAPI/Swagger docs from FastAPI

## Development

### Local Development Setup

#### Backend:
```bash
cd backend
pip install -r requirements.txt
uvicorn src.api.main:app --reload
```

#### Frontend:
```bash
cd docusaurus
npm install
npm run start
```

## Contributing

Please follow the patterns established in the existing codebase. All new features should follow the Spec-Driven Development approach outlined in the project constitution.