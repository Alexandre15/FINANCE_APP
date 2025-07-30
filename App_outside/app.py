from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')  # Ou render_template se preferir

@app.route('/usuarios', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'POST':
        data = request.get_json()
        novo_usuario = Usuario(nome=data['nome'], email=data['email'])
        try:
            db.session.add(novo_usuario)
            db.session.commit()
            return jsonify({'message': 'Usuário criado com sucesso!'}), 201
        except:
            db.session.rollback()
            return jsonify({'error': 'Erro ao criar usuário (email já existe?)'}), 400
    
    usuarios = Usuario.query.order_by(Usuario.id.desc()).all()
    return jsonify([{'id': u.id, 'nome': u.nome, 'email': u.email} for u in usuarios])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
