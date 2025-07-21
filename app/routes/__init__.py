from flask import jsonify, request, Blueprint
from app import db
from .answers import answers_bp
from .images import image_bp
from app.models import User

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET"])
def check_connection():
    return jsonify({"message": "Success Connect"}), 200

@main_bp.route('/signup', methods=["POST"])
def signup():
    user_data = request.get_json()

    not_null_datas = ['name', 'email', 'age', 'gender']
    for data in not_null_datas:
        if data not in user_data:
            return jsonify({"message": f"{data}는 필수로 입력해주세요."}), 400

    name = data['name']
    email = data['email']
    age = data['age']
    gender = data['gender']

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "이미 존재하는 계정 입니다."}), 400

    new_user = User(name=name, email=email, age=age, gender=gender)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "회원가입이 완료되었습니다."}), 200