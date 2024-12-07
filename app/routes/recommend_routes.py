from flask import Blueprint, request, jsonify
from app.models import users
from app.services.gemini_service import find_common_styles
from app.services.spotify_service import search_recommendations

recommend_bp = Blueprint("recommend", __name__)

@recommend_bp.route('/', methods=['POST'])
def recommend_for_users():
    selected_users = request.json.get("users")
    if not selected_users or len(selected_users) < 2:
        return jsonify({"error": "Selecione pelo menos dois usuários"}), 400

    user_descriptions = [", ".join(user.styles) for user in users if user.username in selected_users]
    common_styles = find_common_styles(user_descriptions)

    recommendations = search_recommendations(common_styles)
    return jsonify(recommendations), 200
