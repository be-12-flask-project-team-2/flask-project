from flask import Blueprint, jsonify
from app.models import Question

questions_blp = Blueprint("questions", __name__, url_prefix="/questions")

# 특정 질문 1개 조회
@questions_blp.route("/<int:question_id>", methods=["GET"])
def get_question(question_id):
    question = Question.query.get(question_id)

    if not question or not question.is_active:
        return jsonify({"message": "Question not found"}), 404

    result = {
        "id": question.id,
        "title": question.title,
        "sqe": question.sqe,
        "image_id": question.image_id,
        "is_active": question.is_active
    }

    return jsonify(result), 200

# 모든 질문 조회
@questions_blp.route("/", methods=["GET"])
def get_all_questions():
    questions = Question.query.filter_by(is_active=True).order_by(Question.sqe).all()

    result = [{
        "id": question.id,
        "title": question.title,
        "sqe": question.sqe,
        "image_id": question.image_id,
        "is_active": question.is_active
    } for question in questions]

    return jsonify(result), 200