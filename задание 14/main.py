from fastapi import FastAPI
from config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.app_debug
)

@app.get("/settings")
def get_settings():
    return {
        "app_name": settings.app_name,
        "app_version": settings.app_version,
        "app_debug": settings.app_debug
    } 