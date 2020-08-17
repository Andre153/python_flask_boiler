from flask import Blueprint, request
from .user import create_new_user, get_user_by_id, get_all_users
from .dto import UserDTO, user_schema, users_schema
import json

user_bp = Blueprint(
    'user_bp', __name__
)


@user_bp.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = get_user_by_id(id)
    return user_schema.dumps(user)


@user_bp.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    return users_schema.dumps(users)


@user_bp.route('/create', methods=['POST'])
def create_user():
    request_data = request.get_json(force=True)['user']
    user_data = UserDTO(
        request_data['username'],
        request_data['email']
    )
    create_new_user(user_data)
    return 200

