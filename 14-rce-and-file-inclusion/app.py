import re
from flask import Flask,request
app=Flask(__name__)
def shell(c):
 return "\n".join("pong "+x.strip()[5:] if x.strip().startswith("ping ") else "FLAG{command_injection}" if x.strip()=="cat flag.txt" else "unknown" for x in c.split(";"))
@app.get("/vuln")
def vuln():return shell("ping "+request.args.get("host",""))
@app.get("/fixed")
def fixed():
 h=request.args.get("host","");return "pong "+h if re.fullmatch(r"[\w.-]+",h) else ("bad host",400)
app.run(port=5000)

