from flask import Flask, request, send_file
from rembg import remove
from io import BytesIO
import os, sys

app = Flask(__name__)

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    if "image" not in request.files:
        return "No image uploaded", 400
    out = remove(request.files["image"].read())
    return send_file(BytesIO(out), mimetype="image/png")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"[*] Starting on port {port}", file=sys.stderr, flush=True)
    app.run(host="0.0.0.0", port=port)
