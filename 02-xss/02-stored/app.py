from flask import Flask, redirect, render_template_string, request

app = Flask(__name__)
comments = ["The first normal comment"]


@app.post("/comments")
def create_comment():
    comments.append(request.form.get("body", ""))
    return redirect("/vuln")


@app.get("/vuln")
def vulnerable_comments():
    rendered = "".join(f"<li>{comment}</li>" for comment in comments)
    return f"<h1>Comments</h1><ul>{rendered}</ul>"


@app.get("/fixed")
def fixed_comments():
    return render_template_string(
        "<h1>Comments</h1><ul>{% for comment in comments %}<li>{{ comment }}</li>{% endfor %}</ul>",
        comments=comments,
    )


app.run(port=5000)
