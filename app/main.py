
from fastapi import FastAPI

app = FastAPI(title="Self-Healing DevOps API")


@app.get("/")
def home():
    return {
        "message": "Self-Healing DevOps API is running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/ready")
def ready():
    return {"status": "ready"}
