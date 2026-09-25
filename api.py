# Creating specific endpoints for AWS and streamlit UI.

## An endpoint which takes input pdf, stores it in a temporary directory on linux file system
## and deletes the output when the split pdf is sent back.
from fastapi import FastAPI, File, UploadFile, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse
from splittingpdfs import read_pdf, write_to_newpdf, output_split_pdf
import tempfile
import pathlib
import shutil

app = FastAPI()

async def delete_file(uploaded_file:UploadFile):
    await uploaded_file.close()

@app.post("/upload/")
async def test_upload_file_endpoint(background_task : BackgroundTasks,
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
    
@app.post("/splitpdf/", response_class=FileResponse)
async def splitting_pdf(start_page:int, 
                        end_page:int,
                        background_task : BackgroundTasks,
                        file:UploadFile | None = None):
    
    if not file:
        return {"message":"No file sent"}
    
    else:
        contents = await file.read()
        temp_dir_path = pathlib.Path(tempfile.mkdtemp())
        input_pdf_path = temp_dir_path / "input.pdf"
        # writing data into a newly created directory
        input_pdf_path.write_bytes(contents)
        try:
            reader = read_pdf(str(input_pdf_path))
            writer = write_to_newpdf(reader,start_page,end_page)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

        output_split_pdf_path = temp_dir_path / "split_pdf.pdf"
        result = output_split_pdf(writer, str(output_split_pdf_path))
        background_task.add_task(shutil.rmtree, temp_dir_path, ignore_errors=True)
        return FileResponse(result, filename="split_pdf")
        

