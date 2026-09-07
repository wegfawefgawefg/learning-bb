from flask import Flask, make_response

app = Flask(__name__)


@app.get("/")
def index():
    response = make_response(
        """
        <h1>Browser storage</h1>
        <button onclick="showStorage()">Show JavaScript-readable storage</button>
        <pre id="output"></pre>
        <script>
          localStorage.setItem("local_demo", "persists across browser restarts");
          sessionStorage.setItem("tab_demo", "belongs to this tab");
          function showStorage() {
            document.querySelector("#output").textContent = JSON.stringify({
              documentCookie: document.cookie,
              localStorage: localStorage.getItem("local_demo"),
              sessionStorage: sessionStorage.getItem("tab_demo")
            }, null, 2);
          }
        </script>
        """
    )
    response.set_cookie("readable_cookie", "visible-to-javascript")
    response.set_cookie(
        "session", "hidden-from-javascript", httponly=True, samesite="Lax"
    )
    return response


app.run(port=5000)
