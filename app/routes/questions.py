from flask import Blueprint

questions_bp = Blueprint("questions", __name__, url_prefix="/questions")

@questions_bp.route("/")
def questions():
    return "questions 연결 완료."