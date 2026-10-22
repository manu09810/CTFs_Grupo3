from flask import Flask, request, render_template
import os

app = Flask(__name__)

FLAG = os.environ.get("CTF_FLAG", "flag{reflected_xss_grupo3}")

@app.route("/", methods=["GET"])
def index():
    name = request.args.get("name", "")
    return render_template("index.html", name=name, flag=FLAG)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
