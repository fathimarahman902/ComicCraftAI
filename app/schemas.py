from fastapi.responses import StreamingResponse
from fpdf import FPDF
import requests
from io import BytesIO

@router.get("/download-pdf")
def download_comic_pdf(story: str = "A fun adventure"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    pdf.set_font("Arial", "B", 20)
    pdf.cell(0, 10, "ComicCraftAI - Your AI Comic", ln=True, align="C")
    pdf.ln(10)
    
    for i in range(1, 6):
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, f"Panel {i}: A fun adventure - Part {i}", ln=True)
        
        # Image from pollinations
        img_url = f"https://image.pollinations.ai/prompt/{story}%20comic%20panel%20{i}%20cartoon?width=400&height=300&seed={i}"
        try:
            r = requests.get(img_url, timeout=10)
            img_bytes = BytesIO(r.content)
            pdf.image(img_bytes, x=10, w=190)
        except:
            pdf.cell(0, 10, f"[Image {i}]", ln=True)
        
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 8, f"{story} - Part {i}")
        pdf.ln(10)

    pdf_bytes = BytesIO(pdf.output())
    pdf_bytes.seek(0)
    
    return StreamingResponse(pdf_bytes, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=comic.pdf"})