import requests

base_url = "http://127.0.0.1:5000"
alice_session = {"Authorization": "Bearer alice-session"}

for path in ("vuln/1", "vuln/2", "fixed/1", "fixed/2"):
    response = requests.get(f"{base_url}/{path}", headers=alice_session)
    print(path, response.status_code, response.text)
