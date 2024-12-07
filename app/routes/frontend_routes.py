from flask import Blueprint, render_template

frontend_bp = Blueprint("frontend", __name__)

@frontend_bp.route('/')
def about_page():
    return render_template("about.html", title="Sobre o MusicMate")

@frontend_bp.route('/register')
def register_page():
    return render_template("register.html", title="Cadastro de Usuário")

@frontend_bp.route('/recommend')
def recommend_page():
    return render_template("recommend.html", title="Recomendações")
