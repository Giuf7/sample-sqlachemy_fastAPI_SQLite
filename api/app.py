from fastapi import FastAPI
from dal.database import engine, Base
from dal.models import User, Exemple  # noqa: F401 — ensures models are registered before create_all
from api.routes import user_router, exemple_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sample FastAPI + SQLAlchemy + SQLite", version="1.0.0")

app.include_router(user_router, prefix="/api/v1")
app.include_router(exemple_router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "API is running", "docs": "/docs"}
