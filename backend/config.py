import os

# Switch to PostgreSQL by changing this one line:
# DATABASE_URL = "postgresql://user:password@localhost/workflow_engine"
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./workflow_engine.db")

APP_TITLE = "Halleyx Workflow Engine API"
APP_VERSION = "1.0.0"
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:5173,http://localhost:3000").split(",")
