from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router

app = FastAPI(title="Real Estate AI Agent")

# Enable CORS to allow frontend (HTML/JS) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],              # Allow all origins (use specific ones in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all routes from app/api/routes.py
app.include_router(api_router)
