from flask import Flask, request, jsonify, render_template
from typing import Union

app = Flask(__name__)

@app.route("/", methods=["GET"])
def read_root():
    return render_template("home.html")

@app.route("/items/<int:item_id>", methods=["GET"])
def read_item(item_id: int):
    q = request.args.get("q")
    data = {"item_id": item_id, "q": q}
    return render_template("home.html", data=data)

if __name__ == "__main__":
    app.run()