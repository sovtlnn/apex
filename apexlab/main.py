from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(title="Apex Lab")

# Serve static assets (CSS, JS, images if added later)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def root():
    html = Path("templates/index.html").read_text()
    return HTMLResponse(content=html)


@app.get("/health")
async def health():
    return {"status": "ok", "service": "apex-lab"}
