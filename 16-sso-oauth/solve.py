import requests

b = "http://127.0.0.1:5000"
print(requests.get(b + "/vuln/callback", params={"code": "foreign-flow"}).text)
print(
    requests.get(
        b + "/fixed/callback", params={"code": "foreign-flow", "state": "fake"}
    ).status_code
)
