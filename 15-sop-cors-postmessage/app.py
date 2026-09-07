from flask import Flask,jsonify,request
app=Flask(__name__)
@app.get("/vuln")
def vuln():
 r=jsonify(secret="FLAG{cors}");r.headers["Access-Control-Allow-Origin"]=request.headers.get("Origin","*");r.headers["Access-Control-Allow-Credentials"]="true";return r
@app.get("/fixed")
def fixed():
 r=jsonify(secret="data")
 if request.headers.get("Origin")=="https://app.test":r.headers["Access-Control-Allow-Origin"]="https://app.test";r.headers["Vary"]="Origin"
 return r
app.run(port=5000)

