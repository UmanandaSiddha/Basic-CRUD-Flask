from flask import Blueprint, jsonify, request
from models.user import User
from __init__ import db
from controllers.user_controller import get_all_users, create_new_user, get_user_by_id, update_user, delete_user

bp = Blueprint('users', __name__)

@bp.route('/api/users', methods=['GET'])
def fetch_users():
    users_list = get_all_users()
    return jsonify(users_list), 200

@bp.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    user = create_new_user(data['name'], data['email'])
    return jsonify({"message": "User created", "user": user }), 201

@bp.route('/api/users/<int:user_id>', methods=['GET'])
def get_user_byId_route(user_id):
    user = get_user_by_id(user_id)
    return jsonify({"message": "User Fetched By Id", "user": user }), 201

@bp.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    data = request.json
    updated_user = update_user(user_id, data['name'])
    if updated_user:
        return jsonify({"message": "User updated", "user": updated_user}), 200
    else:
        return jsonify({"error": "User not found"}), 404

@bp.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    result = delete_user(user_id)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"error": "User not found"}), 404