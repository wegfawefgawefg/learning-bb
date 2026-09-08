from pathlib import Path
from flask import Flask, request

app = Flask(__name__)
root = Path(__file__).with_name("exports")
root.mkdir(exist_ok=True)
(root / "alice.csv").write_text("item,total\nnotebook,25")
Path(__file__).with_name("backup.env").write_text("FLAG{download_boundary}")


@app.get("/account/exports/download")
def download():
    return (root / request.args.get("file", "alice.csv")).read_text()


app.run(port=5000)
