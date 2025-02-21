from flask import Flask
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Blueprint Registration
    from app.blueprints.projects import bp_project
    app.register_blueprint(bp_project)

    return app