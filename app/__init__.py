from config.settings import Config

from app.routes import blueprint
from app.db import db

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(blueprint=blueprint)

    db.init_app(app=app)

    with app.app_context():
        db.create_all()

    return app
