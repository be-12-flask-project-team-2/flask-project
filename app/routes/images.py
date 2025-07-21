from flask import Flask, jsonify, Blueprint

image_bp = Blueprint("image", __name__, url_prefix="/images")

@image_bp.route("/main", methods=["GET"])
def get_image():
    return jsonify({"image": "https://images.unsplash.com/photo-1614522407266-ad3c5fa6bc24?q=80&w=1473&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"})

