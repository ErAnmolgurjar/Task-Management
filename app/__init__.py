from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.tasks import task_bp

    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(task_bp, url_prefix="/api")

    with app.app_context():
        db.create_all()

    return app
