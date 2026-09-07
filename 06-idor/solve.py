import requests

for p in ("vuln/2", "fixed/2"):
    r = requests.get("http://127.0.0.1:5000/" + p, headers={"X-User": "alice"})
    print(p, r.status_code, r.text)
