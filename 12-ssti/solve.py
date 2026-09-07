import requests

for p in ("vuln", "fixed"):
    r = requests.get("http://127.0.0.1:5000/" + p, params={"name": "{{7*7}}"})
    print(p, r.text)
