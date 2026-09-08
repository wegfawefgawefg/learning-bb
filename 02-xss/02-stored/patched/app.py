from flask import Flask, redirect, render_template_string, request

app = Flask(__name__)
feedback = []


@app.post("/feedback")
def submit():
    feedback.append(request.form.get("message", ""))
    return redirect("/thanks")


@app.get("/thanks")
def thanks():
    return "<!doctype html><p>Thanks. A moderator will review your message.</p>"


@app.get("/moderation")
def moderation():
    return render_template_string(
        "<!doctype html><h1>Moderation queue</h1>{% for message in feedback %}<article>{{ message }}</article>{% endfor %}",
        feedback=feedback,
    )


app.run(port=5000)
