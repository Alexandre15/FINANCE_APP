from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/")
def index():
    # Dados de exemplo para a diversificação do patrimônio
    data = {
        "labels": ["Ações", "Renda Fixa", "Imóveis", "Criptomoedas", "Caixa"],
        "series": [40, 25, 20, 10, 5]
    }
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
