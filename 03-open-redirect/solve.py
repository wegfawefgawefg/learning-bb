import requests
r=requests.get("http://127.0.0.1:5000/vuln",params={"next":"https://example.test"},allow_redirects=False)
print(r.status_code,r.headers["Location"])

