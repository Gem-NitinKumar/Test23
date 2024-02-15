from flask import Flask
from app.views.blueprint import blueprint_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint_bp)
    return app
