from flask import Flask
from flask_assets import Environment


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('setup.Config')
    assets = Environment()
    assets.init_app(app)

    with app.app_context():
        from .user import user

        app.register_blueprint(user.user_bp)

        return app
