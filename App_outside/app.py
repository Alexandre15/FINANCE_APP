from flask import Flask, render_template, jsonify
import pandas as pd
# from sqlalchemy import create_engine, Column, Integer, String

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route('/dados')
def dados():
    df = pd.read_excel('dados.xlsx')
    dados_json = df.to_dict(orient='records')
    return jsonify(dados_json)


if __name__ == "__main__":
    app.run(debug=True)
