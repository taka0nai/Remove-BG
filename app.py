from flask import Flask, request, send_file
from rembg import remove
from io import BytesIO
import os

app = Flask(__name__)

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    if "image" not in request.files:
        return "No image uploaded", 400
    output = remove(request.files["image"].read())
    return send_file(BytesIO(output), mimetype="image/png")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))   # <- use Render-supplied port
    app.run(host="0.0.0.0", port=port)
