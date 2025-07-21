from flask import Blueprint, render_template
from .users import users_bp
from .questions import questions_bp
from .answers import answers_bp

main_bp = Blueprint("main", __name__)

main_bp.register_blueprint(users_bp)
main_bp.register_blueprint(questions_bp)
main_bp.register_blueprint(answers_bp)

@main_bp.route("/")
def main():
    return render_template("main.html")