from flask import jsonify, request, Blueprint
from .answers import answers_blp
from .choices import choices_blp
from .questions import questions_blp
from .stats_routes import stats_routes_blp
from .users import user_blp
from .images import images_blp

main_bp = Blueprint("main", __name__)

def register_routes(application):
    main_bp.register_blueprint(user_blp)
    main_bp.register_blueprint(images_blp, url_prefix="/image")
    main_bp.register_blueprint(questions_blp, url_prefix="/questions")
    main_bp.register_blueprint(choices_blp, url_prefix="/choices")
    main_bp.register_blueprint(stats_routes_blp)
    main_bp.register_blueprint(answers_blp)

    application.register_blueprint(main_bp)