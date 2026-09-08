from pathlib import Path
from flask import Flask, request

app = Flask(__name__)
root = Path(__file__).with_name("documents")
root.mkdir(exist_ok=True)
(root / "welcome.txt").write_text("Welcome")
Path(__file__).with_name("application.env").write_text("FLAG{include_crosses_directory}")


@app.get("/documents/view")
def view():
    return (root / request.args.get("template", "welcome.txt")).read_text()


app.run(port=5000)
