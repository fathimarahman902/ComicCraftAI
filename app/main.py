from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# Correct path - inga thaan mistake nadanthuchu
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

app.mount("/templates", StaticFiles(directory=TEMPLATE_DIR), name="templates")

@app.get("/", response_class=HTMLResponse)
def home():
    with open(os.path.join(TEMPLATE_DIR, "index.html"), "r", encoding="utf-8") as f:
        return f.read()

@app.api_route("/generate", methods=["GET", "POST"], response_class=HTMLResponse)
def generate():
    with open(os.path.join(TEMPLATE_DIR, "result.html"), "r", encoding="utf-8") as f:
        return f.read()