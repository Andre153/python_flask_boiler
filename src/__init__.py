from flask import Flask
from flask_assets import Environment
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
marsh = Marshmallow()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('setup.DevelopConfig')
    assets = Environment()
    assets.init_app(app)
    db.init_app(app)
    marsh.init_app(app)

    with app.app_context():
        from .user import routes
        app.register_blueprint(routes.user_bp)
        from .user.model import User

        db.create_all()
        return app
