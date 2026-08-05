from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socket
import os

app = FastAPI(title="AWS CI/CD Demo")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Backend is updated successfully",
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENV", "Development")
    }

@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }

@app.get("/users")
def users():
    return [
        {
            "id": 1,
            "name": "John"
        },
        {
            "id": 2,
            "name": "Alice"
        },
        {
            "id": 3,
            "name": "David"
        }
    ]