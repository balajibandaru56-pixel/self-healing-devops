
from fastapi import FastAPI
from datetime import datetime, timezone
import os
import time

app = FastAPI(title="Self-Healing DevOps API")

START_TIME = time.time()
VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.get("/")
def home():
    return {
        "project": "Self-Healing DevOps Platform",
        "version": VERSION,
        "message": "Application is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "version": VERSION
    }


@app.get("/ready")
def ready():
    return {"status": "ready"}


@app.get("/metrics-info")
def metrics_info():
    return {
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "version": VERSION
    }