from flask import Blueprint, request, jsonify
from services.user_service import validate_login

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body is required"
        }), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "success": False,
            "message": "Email and password are required"
        }), 400

    if validate_login(email, password):
        return jsonify({
            "success": True,
            "message": "Login successful",
            "user": {
                "email": email
            }
        }), 200

    return jsonify({
        "success": False,
        "message": "Invalid email or password"
    }), 401