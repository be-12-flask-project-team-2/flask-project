from flask import Flask, jsonify, Blueprint, request
from config import db
from app.models import Answer

answers_blp = Blueprint("answers", __name__)

@answers_blp.route("/submit", methods=["POST"])
def submit_answers():
    data = request.get_json()
    user_id = data[0]["user_id"]
    for item in data:
        answer = Answer(user_id=item["user_id"], choice_id=item["choice_id"])
        db.session.add(answer)

    db.session.commit()
    return jsonify({"message": f"User: {user_id}'s answers Success Create"}), 200