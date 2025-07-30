from flask import Flask, render_template, request, redirect, session, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Book, Food, Movie
import bcrypt

app = Flask(__name__)
app.secret_key = 'segredo_super_seguro'

# Conexão com o banco de dados
engine = create_engine('sqlite:///database.db', echo=True)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
db_session = DBSession()

# Rotas


@app.route('/')
def index():
    if "user_id" not in session:
        return redirect(url_for("login"))

    user = db_session.query(User).filter_by(id=session["user_id"]).first()
    return render_template("home.html", user=user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        raw_password = request.form['password']
        hashed = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())

        if db_session.query(User).filter_by(username=username).first():
            return "Usuário já existe"

        user = User(username=username, password=hashed)
        db_session.add(user)
        db_session.commit()
        return redirect(url_for('login'))

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        raw_password = request.form['password']

        user = db_session.query(User).filter_by(username=username).first()
        if user and bcrypt.checkpw(raw_password.encode('utf-8'), user.password):
            session['user_id'] = user.id
            return redirect(url_for('index'))
        return "Login inválido"

    return render_template("login.html")


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/add', methods=['POST'])
def add():
    if "user_id" not in session:
        return redirect(url_for("login"))

    user = db_session.query(User).filter_by(id=session["user_id"]).first()
    tipo = request.form["tipo"]
    valor = request.form["valor"]

    if tipo == "book":
        db_session.add(Book(title=valor, user=user))
    elif tipo == "food":
        db_session.add(Food(name=valor, user=user))
    elif tipo == "movie":
        db_session.add(Movie(title=valor, user=user))

    db_session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
