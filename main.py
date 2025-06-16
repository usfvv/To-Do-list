from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI(title="Simple To-Do App")

# ثبت قاعدة البيانات وباقي الكود API هنا (زي ما انت عامل)

# ربط فولدر static
app.mount("/static", StaticFiles(directory="static"), name="static")

# endpoint لعرض صفحة الـ HTML
@app.get("/", response_class=HTMLResponse)
async def read_index():
    file_path = os.path.join("static", "index.html")
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)