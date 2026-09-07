from urllib.parse import quote

payload = '<img src="/missing-image" onerror="alert(`DOM XSS`)">'
fragment = quote(payload)

print(f"Vulnerable: http://127.0.0.1:5000/vuln#{fragment}")
print(f"Fixed:      http://127.0.0.1:5000/fixed#{fragment}")
