import os
from flask import Flask
from app.routes import main_bp

def create_app():
    template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../templates')
    app = Flask(__name__, template_folder=template_path)
    app.register_blueprint(main_bp)
    return app