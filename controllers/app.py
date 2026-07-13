from uuid import uuid4

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

sessions = {}

app.mount("/assets", StaticFiles(directory="ui/dist/assets"), name="assets")


@app.get("/")
async def home():
    return FileResponse("ui/dist/index.html")


@app.post("/session")
def create_session():

    session_id = str(uuid4())

    sessions[session_id] = {
        "messages": [],
        "documents": []
    }

    return {
        "session_id": session_id
    }


@app.post("/upload/{session_id}")
async def upload_files(
    session_id: str,
    files: list[UploadFile] = File(...)
):

    if session_id not in sessions:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    uploaded = []

    for file in files:

        content = await file.read()

        sessions[session_id]["documents"].append({
            "filename": file.filename,
            "content": content
        })

        uploaded.append(file.filename)

    return {
        "uploaded": uploaded
    }
