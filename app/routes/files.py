from fastapi import APIRouter, HTTPException
from pathlib import Path
from fastapi.responses import FileResponse
import os


files_router = APIRouter()

@files_router.get("/download/{file_name}.{file_type}/{file_id}")
def download(file_name: str, file_type: str, file_id: str):
    pdf_dir = Path(__file__).parent.parent.parent / 'files'
    file_path = Path(f'{pdf_dir}/{file_id}.{file_type}')
    if not file_path.exists():
        print(f"{file_id}.{file_type} not found at {file_path}")
        raise HTTPException(status_code=404, detail=f"{file_id}.{file_type} not found")
    
    
    return FileResponse(file_path, filename=file_name, media_type=f'application/{file_type}')
