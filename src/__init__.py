from flask import Flask
from flask_assets import Environment
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    print("creating app")
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('setup.DevelopConfig')
    assets = Environment()
    assets.init_app(app)
    db.init_app(app)

    with app.app_context():
        from .user import user
        app.register_blueprint(user.user_bp)
        from .user.model import User

        db.create_all()
        return app
