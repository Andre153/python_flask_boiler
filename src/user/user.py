from flask import Blueprint, render_template

user_bp = Blueprint(
    'user_bp', __name__
)


@user_bp.route('/profile', methods=['GET'])
def user_profile():
    return 'testing_user'
