# resume.py

from fastapi import APIRouter, UploadFile
from app.services.analyze_service import analyze_resume

router= APIRouter()
# creating a gorup of routers, not another app=fastapi()

@router.get("/")
def root():
    return {
        "message":"Resume reader is running"
    }

@router.post("/analyze")
async def upload_resume(file:UploadFile):
    contents = await file.read()
    file_path= f"uploads/{file.filename}"
    with open(file_path,"wb") as f:
        f.write(contents)
    return analyze_resume(file_path)
