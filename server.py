from sqlite3.dbapi2 import connect
import time as t
import json
import sqlite3

from flask import Flask, render_template, request, Response

app = Flask(__name__, static_folder="public")


@app.route("/")
def serve_route():
    return render_template("main.html")


@app.route("/register", methods=["POST"])
def api_register():
    req_data = json.loads(request.data.decode(request.charset))

    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute(
        "create table if not exists todo("
        "time integer, "
        "title text,"
        "detail title"
        ")"
    )

    cursor.execute(
        "insert into todo values (:time, :title, :detail)",
        {
            "time": t.time(),
            "title": req_data["title"],
            "detail": req_data["detail"]
        }
    )

    conn.commit()

    return Response(status=200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=3000, )
