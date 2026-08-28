from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from jobmatcher.routes.auth import router as auth_router
from jobmatcher.routes.cv import router as cv_router
from jobmatcher.routes.health import router as health_router
from jobmatcher.routes.jobs import router as jobs_router
from jobmatcher.routes.profile import router as profile_router
from jobmatcher.routes.recommendations import (
    router as recommendations_router,
)


app = FastAPI(
    title="JobMatcher",
    description=(
        "API for CV analysis, "
        "job matching and recommendations."
    ),
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    health_router
)

app.include_router(
    auth_router
)

app.include_router(
    cv_router
)

app.include_router(
    jobs_router
)

app.include_router(
    profile_router
)

app.include_router(
    recommendations_router
)

@app.get("/")
def root():
    return {
        "name": "JobMatcher",
        "version": "1.0.0",
        "status": "running",
    }

