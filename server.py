from flask import Flask, render_template

app = Flask(__name__, static_folder="public")


@app.route("/")
def serve_route():
    return render_template("main.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=3000, )
