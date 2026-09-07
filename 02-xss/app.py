from flask import Flask,request,render_template_string
app=Flask(__name__)
@app.get("/vuln")
def vuln():return render_template_string("<p>"+request.args.get("q","")+"</p>")
@app.get("/fixed")
def fixed():return render_template_string("<p>{{q}}</p>",q=request.args.get("q",""))
app.run(port=5000)

