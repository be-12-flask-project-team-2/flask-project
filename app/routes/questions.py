from flask import Blueprint, render_template

questions_bp = Blueprint("questions", __name__, url_prefix="/questions")

@questions_bp.route("/")
def questions():
    return render_template("survey.html")