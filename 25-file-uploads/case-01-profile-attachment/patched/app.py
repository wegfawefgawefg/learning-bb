import secrets
from pathlib import Path
from flask import Flask, request, send_from_directory

app = Flask(__name__)
uploads = Path(__file__).with_name("uploads")
uploads.mkdir(exist_ok=True)


@app.post("/api/profile/attachment")
def upload():
    file = request.files["file"]
    if file.mimetype not in ("image/png", "image/jpeg"):
        return {"error": "image required"}, 400
    name = secrets.token_hex(16) + (".png" if file.mimetype == "image/png" else ".jpg")
    file.save(uploads / name)
    return {"url": "/uploads/" + name}


@app.get("/uploads/<name>")
def serve(name):
    return send_from_directory(uploads, name, as_attachment=True)


app.run(port=5000)
