from flask import Blueprint, render_template

answers_bp = Blueprint("answers", __name__, url_prefix="/answers")

@answers_bp.route("/")
def answers():
    return render_template("answers.html")