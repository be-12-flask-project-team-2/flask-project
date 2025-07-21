from flask import jsonify, request, Blueprint
# from app.models import User
# from .answers import answers_blp
# from .choices import choices_blp
from .questions import questions_blp
from .stats_routes import stats_routes_blp
from .users import user_blp
from .images import images_blp

main_bp = Blueprint("main", __name__)

# def register_routes(application):
#     # 코드 작성

@main_bp.route("/", methods=["GET"])
def check_connection():
    return jsonify({"message": "Success Connect"}), 200