import requests

b = "http://127.0.0.1:5000"
print(requests.post(b + "/vuln/buy", data={"item": "1", "price": "1"}).text)
print(requests.get(b + "/vuln/admin", params={"role": "admin"}).text)
