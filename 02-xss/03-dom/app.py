from flask import Flask

app = Flask(__name__)


@app.get("/vuln")
def vulnerable_page():
    return """
        <h1 id="output"></h1>
        <script>
          const name = decodeURIComponent(location.hash.slice(1));
          document.querySelector("#output").innerHTML = "Hello " + name;
        </script>
    """


@app.get("/fixed")
def fixed_page():
    return """
        <h1 id="output"></h1>
        <script>
          const name = decodeURIComponent(location.hash.slice(1));
          document.querySelector("#output").textContent = "Hello " + name;
        </script>
    """


app.run(port=5000)
