from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from PIL import Image
import os

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {})

@router.api_route("/generate", methods=["GET", "POST"])
async def generate(request: Request):
    return templates.TemplateResponse(request, "result.html", {})

@router.get("/download-pdf")
async def download_pdf():
    # PDF create pannuthu
    img_path = "static/fox_final.png"
    if not os.path.exists(img_path):
        return HTMLResponse("<h1>fox_final.png-a static folder la podunga pa!</h1>")
    
    img = Image.open(img_path).convert("RGB")
    pdf_path = "static/fox_comic.pdf"
    img.save(pdf_path, "PDF", resolution=150)
    return FileResponse(pdf_path, filename="Fox_Comic.pdf", media_type="application/pdf")

@router.get("/health")
async def health():
    return {"status": "ok"}