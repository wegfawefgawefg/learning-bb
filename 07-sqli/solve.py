import requests

for p in ("vuln", "fixed"):
    r = requests.get("http://127.0.0.1:5000/" + p, params={"name": "' OR 1=1 -- "})
    print(p, r.text)
