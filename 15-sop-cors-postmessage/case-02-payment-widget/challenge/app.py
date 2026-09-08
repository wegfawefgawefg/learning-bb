from flask import Flask

app = Flask(__name__)


@app.get("/widget")
def widget():
    return """<!doctype html><script>addEventListener('message',event=>{if(event.data.action==='payment-status')event.source.postMessage({status:'paid',receipt:'FLAG{message_leak}'},'*')})</script><h1>Payment widget</h1>"""


app.run(port=5000)
