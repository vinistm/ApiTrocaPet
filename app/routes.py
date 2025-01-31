from flask import jsonify, request
from app import app, db
from app.models import Usuario
from app.services import validar_senha, gerar_token_jwt

@app.route('/cadastro', methods=['POST'])
def cadastro():
    dados = request.get_json()
    if not dados or 'nome' not in dados or 'email' not in dados or 'senha' not in dados:
        return jsonify({'erro': 'Dados inválidos'}), 400

    if not validar_senha(dados['senha']):
        return jsonify({'erro': 'Senha inválida. A senha deve ter pelo menos 6 caracteres, '
                                'uma letra maiúscula, um número e um símbolo especial.'}), 400

    if Usuario.query.filter_by(email=dados['email']).first():
        return jsonify({'erro': 'Email já cadastrado'}), 400

    usuario = Usuario(nome=dados['nome'], email=dados['email'])
    usuario.set_senha(dados['senha'])
    db.session.add(usuario)
    db.session.commit()

    token = gerar_token_jwt(usuario.id)
    return jsonify({'token': token}), 201

@app.route('/login', methods=['POST'])
def login():
    dados = request.get_json()
    if not dados or 'email' not in dados or 'senha' not in dados:
        return jsonify({'erro': 'Dados inválidos'}), 400

    usuario = Usuario.query.filter_by(email=dados['email']).first()
    if not usuario or not usuario.check_senha(dados['senha']):
        return jsonify({'erro': 'Email ou senha inválidos'}), 401

    token = gerar_token_jwt(usuario.id)
    return jsonify({'token': token}), 200