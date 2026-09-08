from flask import Flask, render_template_string, request

app = Flask(__name__)


@app.post("/api/campaigns/preview")
def preview():
    return render_template_string(
        "<h1>{{greeting}}, Alice</h1>", greeting=request.get_json()["greeting"]
    )


app.run(port=5000)
