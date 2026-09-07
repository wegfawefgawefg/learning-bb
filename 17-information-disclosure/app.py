from pathlib import Path
from flask import Flask,abort,request
app=Flask(__name__);root=Path("public");root.mkdir(exist_ok=True);(root/"hello.txt").write_text("hello");Path("secret.txt").write_text("FLAG{traversal}")
@app.get("/vuln")
def vuln():return (root/request.args.get("name","hello.txt")).read_text()
@app.get("/fixed")
def fixed():
 c=(root/request.args.get("name","hello.txt")).resolve()
 if root.resolve() not in c.parents:abort(400)
 return c.read_text()
app.run(port=5000)

