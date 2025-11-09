from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db import Base, engine
from app.routers import auth, notes
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.security import HTTPBearer
from fastapi.openapi.models import HTTPBearer as HTTPBearerModel

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    print("App shutting down...")

app = FastAPI(lifespan=lifespan)

# Routers
app.include_router(auth.router)
app.include_router(notes.router)

@app.get("/")
def read_root():
    return {"message": "FastAPI Notes App is running"}

# ✅ Add Bearer authentication to OpenAPI (so Swagger shows Authorize button)
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FastAPI Notes App",
        version="1.0.0",
        description="A simple FastAPI Notes app with JWT auth",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
