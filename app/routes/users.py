from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from app.models import User
from config import db

user_blp = Blueprint("users", __name__)

@user_blp.route("/", methods=["POST", "GET"])
def check_connection():
    return jsonify({"message": "Success Connect"}), 200

@user_blp.route("/signup", methods=["POST"])
def signup_page():
    if request.method == "POST":
        try:
            data = request.get_json()

            # 필수 필드 체크
            required_fields = ["name", "age", "gender", "email"]
            for field in required_fields:
                if field not in data:
                    return jsonify({"message": f"Missing required field: {field}"}), 400

            # age enum 값 검증
            valid_ages = ['teen', 'twenty', 'thirty', 'forty', 'fifty']
            if data["age"] not in valid_ages:
                return jsonify({"message": f"Invalid age value. Must be one of: {', '.join(valid_ages)}"}), 400

            # gender enum 값 검증
            valid_genders = ['male', 'female']
            if data["gender"] not in valid_genders:
                return jsonify({"message": f"Invalid gender value. Must be one of: {', '.join(valid_genders)}"}), 400

            # name 길이 검증 (모델에서 String(10)으로 제한됨)
            if len(data["name"]) > 10:
                return jsonify({"message": "Name must be 10 characters or less"}), 400

            # email 길이 검증 (모델에서 String(120)으로 제한됨)
            if len(data["email"]) > 120:
                return jsonify({"message": "Email must be 120 characters or less"}), 400

            user = User(
                name=data["name"],
                age=data["age"],
                gender=data["gender"],
                email=data["email"],
            )

            db.session.add(user)
            db.session.commit()

            return (
                jsonify(
                    {
                        "message": f"{user.name}님 회원가입을 축하합니다",
                        "user_id": user.id,
                    }
                ),
                201,
            )

        except KeyError as e:
            db.session.rollback()
            return jsonify({"message": f"Missing required field: {str(e)}"}), 400

        except IntegrityError as e:
            db.session.rollback()
            # IntegrityError의 구체적인 원인에 따라 메시지 분기
            error_msg = str(e.orig).lower()
            if 'email' in error_msg:
                return jsonify({"message": "이미 존재하는 이메일 입니다."}), 400
            else:
                return jsonify({"message": "데이터 무결성 오류가 발생했습니다."}), 400

        except Exception as e:
            db.session.rollback()
            return jsonify({"message": "서버 오류가 발생했습니다."}), 500