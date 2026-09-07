import requests

for p in ("vuln", "fixed"):
    r = requests.patch("http://127.0.0.1:5000/" + p, json={"role": "admin"})
    print(p, r.status_code, r.text)
