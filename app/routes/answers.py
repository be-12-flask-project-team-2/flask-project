from flask import Blueprint

answers_bp = Blueprint("answers", __name__, url_prefix="/answers")

@answers_bp.route("/")
def answers():
    return "answers 연결 완료."