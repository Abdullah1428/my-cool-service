from flask import Blueprint, request, jsonify
from app.services.opa import check_opa

users_blueprint = Blueprint('users', __name__)

users = []

def validate_email(email):
    import re
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(regex, email)

@users_blueprint.route('/users', methods=['GET'])
def get_users():
    role = request.headers.get('Role')
    if not role or not check_opa(role, request.method):
        return jsonify({"message": "Unauthorized"}), 403
    return jsonify(users)

@users_blueprint.route('/users', methods=['POST'])
def create_user():
    role = request.headers.get('Role')
    if not role or not check_opa(role, request.method):
        return jsonify({"message": "Unauthorized"}), 403
    try:
        user = request.json
        if 'name' not in user or 'email' not in user or not validate_email(user['email']):
            return {"error": "Invalid input"}, 400
        users.append(user)
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        return jsonify({"message": "Bad Request", "error": str(e)}), 400
