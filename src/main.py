import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from .api import app

app.mount("/static", StaticFiles(directory="src/static"), name="static")

@app.get("/")
async def read_root():
    """Sert la page d'accueil"""
    return FileResponse("src/static/index.html")

def main():
    """Lance l'application"""
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
