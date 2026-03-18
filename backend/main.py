from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import APP_TITLE, APP_VERSION
from database import engine
from models import Base
from routes import workflows, steps, rules, executions

# Create all tables on startup (safe to run multiple times — skips existing tables)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    description="Workflow automation engine with dynamic rule evaluation",
)

# Allow all origins in development so the frontend can always reach the backend
# regardless of port or proxy setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(workflows.router)
app.include_router(steps.router)
app.include_router(rules.router)
app.include_router(executions.router)


@app.get("/health")
def health():
    return {"status": "ok", "version": APP_VERSION}
