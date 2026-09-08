from flask import Flask

app = Flask(__name__)


@app.get("/widget")
def widget():
    return """<!doctype html><script>addEventListener('message',event=>{if(event.origin!=='http://127.0.0.1:5000'||event.data?.action!=='payment-status')return;event.source.postMessage({status:'paid'},event.origin)})</script><h1>Payment widget</h1>"""


app.run(port=5000)
