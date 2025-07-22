from flask import Blueprint, request, jsonify
from app import db
from app.models import Choice

choices_blp = Blueprint("choices", __name__)

# 선택지 생성
@choices_blp.route("/", methods=["POST"])
def create_choice():
    data = request.get_json()

    if not data or "question_id" not in data or "content" not in data:
        return jsonify({"message": "Missing required fields"}), 400

    choice = Choice(
        content=data["content"],
        question_id=data["question_id"],
        is_active=data.get("is_active", True),
        sqe=data.get("sqe", 1)
    )

    db.session.add(choice)
    db.session.commit()

    return jsonify({
        "message": "Choice successfully created",
        "choice": {
            "id": choice.id,
            "content": choice.content,
            "question_id": choice.question_id,
            "is_active": choice.is_active,
            "sqe": choice.sqe
        }
    }), 201

# 특정 질문의 선택지 조회
@choices_blp.route("/question/<int:question_id>", methods=["GET"])
def get_choices_by_question(question_id):
    choices = Choice.query.filter_by(question_id=question_id, is_active=True).order_by(Choice.sqe).all()

    result = [{
        "id": choice.id,
        "content": choice.content,
        "sqe": choice.sqe,
        "question_id": choice.question_id
    } for choice in choices]

    return jsonify(result), 200

# 모든 선택지 조회
@choices_blp.route("/", methods=["GET"])
def get_all_choices():
    choices = Choice.query.all()

    result = [{
        "id": choice.id,
        "content": choice.content,
        "sqe": choice.sqe,
        "question_id": choice.question_id,
        "is_active": choice.is_active
    } for choice in choices]

    return jsonify(result), 200  # 모든 선택지 조회