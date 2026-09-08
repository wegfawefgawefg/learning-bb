from flask import Flask

app = Flask(__name__)


@app.get("/profile-preview")
def preview():
    return """<!doctype html><h1 id=preview></h1><script>
    const displayName = decodeURIComponent(location.hash.slice(1));
    document.querySelector('#preview').innerHTML = `Preview for ${displayName}`;
    </script>"""


app.run(port=5000)
