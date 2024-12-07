from flask import Flask
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Importar e registrar blueprints
    from .routes.user_routes import user_bp
    from .routes.recommend_routes import recommend_bp
    from .routes.frontend_routes import frontend_bp  # Novo import

    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(recommend_bp, url_prefix='/recommend')
    app.register_blueprint(frontend_bp)  # Registrar o blueprint do front-end

    return app

