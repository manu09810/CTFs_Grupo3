from pathlib import Path
from flask import Flask, render_template, request, send_file, abort, Response
from urllib.parse import unquote
import os

BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR / "documents"
app = Flask(__name__)

CTF_DATA_DIR = (BASE_DIR / "ctf_data").resolve()
PUBLIC_DIR = (CTF_DATA_DIR / "public").resolve()

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/robots.txt")
def robots():
    return Response("User-agent: *\nDisallow: /backup/\nDisallow: /download\n", mimetype="text/plain")

@app.get("/download")
def download():
    name = request.args.get("file", "welcome.txt")
    target = (PUBLIC_DIR / unquote(name)).resolve()
    if not target.is_file():
        abort(404)
    try:
        return send_file(target, as_attachment=True, download_name=target.name)
    except (OSError, ValueError):
        abort(404)

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
