import requests

for v in ["hello", "'", "../", "<x>", "{{7*7}}", "A" * 40, "%00"]:
    r = requests.get("http://127.0.0.1:5000/parse", params={"value": v})
    print(r.status_code, len(r.content), repr(v), r.text)
