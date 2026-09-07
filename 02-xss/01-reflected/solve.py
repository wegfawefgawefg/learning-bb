from urllib.parse import urlencode

payload = '<img src="/missing-image" onerror="alert(document.domain)">'
query = urlencode({"q": payload})

print(f"Vulnerable: http://127.0.0.1:5000/vuln?{query}")
print(f"Fixed:      http://127.0.0.1:5000/fixed?{query}")
