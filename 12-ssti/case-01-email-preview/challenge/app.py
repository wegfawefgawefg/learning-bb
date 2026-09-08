from flask import Flask, render_template_string, request

app = Flask(__name__)
app.config["MAIL_SIGNING_KEY"] = "FLAG{server_template_context}"


@app.post("/api/campaigns/preview")
def preview():
    return render_template_string("<h1>" + request.get_json()["greeting"] + ", Alice</h1>")


app.run(port=5000)
