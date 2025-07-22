from flask import Flask, jsonify, Blueprint, request
from app.models import Image

images_blp = Blueprint("image", __name__, url_prefix="/images")

images = []
image_id_counter = 1

@images_blp.route("/", methods=["POST"])
def create_image():
    global image_id_counter

    data = request.get_json()

    if not data:
        return jsonify({"message": "Invalid request data"}), 400

    image = {
        "url": data["url"],
        "type": data["type"]
    }
    images.append(image)
    image_id_counter += 1

    return jsonify({"message": f"ID: {image['id']} Image Success Create"}), 200

@images_blp.route("/main", methods=["GET"])
def main_image():
    main_image = Image.query.filter_by(type="main").first()
    return jsonify({"image": main_image.url})