from pathlib import Path
from flask import Flask, request, send_from_directory

app = Flask(__name__)
uploads = Path(__file__).with_name("uploads")
uploads.mkdir(exist_ok=True)


@app.post("/api/profile/attachment")
def upload():
    file = request.files["file"]
    file.save(uploads / file.filename)
    return {"url": "/uploads/" + file.filename}


@app.get("/uploads/<path:name>")
def serve(name):
    return send_from_directory(uploads, name)


app.run(port=5000)
