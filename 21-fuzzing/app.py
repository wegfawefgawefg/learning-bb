from flask import Flask,request
app=Flask(__name__)
@app.get("/parse")
def parse():
 v=request.args.get("value","")
 if v=="{{7*7}}":return "unexpected evaluator:49",500
 if len(v)>30:return "too long",413
 return "accepted:"+v
app.run(port=5000)

