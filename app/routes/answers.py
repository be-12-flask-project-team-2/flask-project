from flask import Flask, jsonify, Blueprint

answers_bp = Blueprint("answers", __name__, url_prefix="/answers")

@answers_bp.route("/stats/answer_rate_by_choice", methods=["GET"])
def rate_by_answer():
    return jsonify({
        "question_id": 1,
        "choice_id": 1,
        "answer_count": 5,
        "percentage": 20.0
    })