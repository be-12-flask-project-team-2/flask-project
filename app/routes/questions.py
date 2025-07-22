from flask import Blueprint, jsonify, request
from app.models import Question
from config import db

questions_blp = Blueprint("questions", __name__, url_prefix="/questions")

@questions_blp.route("/", methods=["POST"])
def create_question():
    data = request.get_json()

    title = data.get("title")
    is_active = data.get("is_active")
    sqe = data.get("sqe")
    image_id = data.get("image_id")

    # 유효성 검사
    if not title or sqe is None or is_active is None:
        return jsonify({"error": "title, sqe, is_active는 필수입니다."}), 400

    # 새 질문 생성
    new_question = Question(
        title=title,
        is_active=is_active,
        sqe=sqe,
        image_id=image_id
    )

    db.session.add(new_question)
    db.session.commit()

    return jsonify({
        "message": f"Title: 새로운 질문 {title} Success Create"
    }), 201

@questions_blp.route("/count", methods=["GET"])
def get_question_count():
    total = db.session.query(Question).count()
    return jsonify({"total": total}), 200

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