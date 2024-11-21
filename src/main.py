import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

os.makedirs("vectorstore", exist_ok=True)

from .api import app

app.mount("/static", StaticFiles(directory="src/static"), name="static")

@app.get("/")
async def read_root():
    """Sert la page d'accueil"""
    return FileResponse("src/static/index.html")

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
