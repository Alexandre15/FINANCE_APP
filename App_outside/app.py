from flask import Flask, render_template
# from sqlalchemy import create_engine, Column, Integer, String

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
