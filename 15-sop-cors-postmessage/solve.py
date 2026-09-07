import requests

for p in ("vuln", "fixed"):
    r = requests.get(
        "http://127.0.0.1:5000/" + p, headers={"Origin": "https://evil.test"}
    )
    print(p, r.headers, r.text)
