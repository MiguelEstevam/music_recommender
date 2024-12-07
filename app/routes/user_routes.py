from flask import Blueprint, request, jsonify
from app.models import users, User

user_bp = Blueprint("user", __name__)

@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get("username")
    styles = data.get("styles")

    if not username or not styles:
        return jsonify({"error": "Nome de usuário e estilos são obrigatórios"}), 400

    user = User(username=username, styles=styles)
    users.append(user)
    return jsonify({"message": "Usuário registrado com sucesso"}), 201

@user_bp.route('/', methods=['GET'])
def get_users():
    return jsonify([{"username": user.username, "styles": user.styles} for user in users]), 200
