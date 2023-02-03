from flask import Flask, request
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = r"./static/pic"
target_file = r""


@app.route("/upload", methods=['POST'])
def upload():
    file_obj = request.files.get("file")
    if file_obj is None:
        return "None"
    file_name = file_obj.filename
    save_path = os.path.join(app.config["UPLOAD_FOLDER"], file_name)
    clear(app.config["UPLOAD_FOLDER"])
    file_obj.save(save_path)
    target_file = save_path


@app.route("/converter", method=["POST"])
def converter():
    pass


@app.route("/download", method=["GET"])
def download():
    pass


def clear(dir):
    if not os.path.exists(dir):
        return False
    if os.path.isfile(dir):
        os.remove(dir)
        return
    for f in os.listdir(dir):
        p = os.path.join(dir, f)
        if os.path.isdir(p):
            clear(p)
        else:
            os.unlink(p)
