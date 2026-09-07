from flask import Flask,jsonify,request
app=Flask(__name__);notes={1:{"owner":"alice","body":"mine"},2:{"owner":"bob","body":"FLAG{idor}"}}
@app.get("/vuln/<int:i>")
def vuln(i):return jsonify(notes.get(i,{}))
@app.get("/fixed/<int:i>")
def fixed(i):
 n=notes.get(i);return jsonify(n) if n and n["owner"]==request.headers.get("X-User") else ("not found",404)
app.run(port=5000)

