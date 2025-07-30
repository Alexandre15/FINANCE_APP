from flask import Flask, render_template
<<<<<<< HEAD
=======
# from flask_sqlalchemy import SQLAlchemy
>>>>>>> 45573d40ff44772042c0b38daea86e29cb66ef9b

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/apexcharts")
def apexcharts():
    # Dados de exemplo para a diversificação do patrimônio
    data = {
        "labels": ["Ações", "Renda Fixa", "Imóveis", "Criptomoedas", "Caixa"],
        "series": [40, 25, 20, 10, 5]
    }
    return render_template("apexcharts.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
