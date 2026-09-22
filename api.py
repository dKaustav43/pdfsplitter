# Creating specific endpoints for AWS and streamlit UI.

## An endpoint which takes input pdf, stores it in a temporary directory on linux file system
## and deletes the output when the split pdf is sent back.

from typing import Annotated
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile | None = None):
    if not file:
        return {"message":"No file sent"}
    else:
        contents = await file.read()
        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "file size": f"{len(contents)/1000} mb"
            }

