import secrets
from flask import Flask,request,session
app=Flask(__name__);app.secret_key="dev"
@app.get("/start")
def start():
 s=secrets.token_urlsafe(12);session["state"]=s;return f'<a href="/fixed/callback?code=alice&state={s}">continue</a>'
@app.get("/vuln/callback")
def vuln():return "logged in with "+request.args.get("code","")
@app.get("/fixed/callback")
def fixed():
 s=session.pop("state",None);return ("logged in with "+request.args.get("code","")) if s and secrets.compare_digest(s,request.args.get("state","")) else ("bad state",403)
app.run(port=5000)

