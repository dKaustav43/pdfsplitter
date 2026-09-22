# Creating specific endpoints for AWS and streamlit UI.

## An endpoint which takes input pdf, stores it in a temporary directory on linux file system
## and deletes the output when the split pdf is sent back.

from typing import Annotated
from fastapi import FastAPI, File, UploadFile, BackgroundTasks

app = FastAPI()

async def delete_file(uploaded_file:UploadFile):
    await uploaded_file.close()

@app.post("/upload/")
async def upload_file(background_task : BackgroundTasks,
                      file: UploadFile | None = None):
    if not file:
        return {"message":"No file sent"}
    else:
        contents = await file.read()
        background_task.add_task(delete_file, file)
        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "file size": f"{len(contents)/1000} mb",
            "message" : "file deleted from memory in the background"
            }
        

