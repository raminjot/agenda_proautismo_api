# Dependecies import
from flask import Blueprint, request, jsonify, json

# Models import
from models import user

# Utils import
from utils import helpers

# Controller initialization
users = Blueprint('users', __name__)


# Endpoints

@users.route('/users/sign_up', methods=['POST'])
def signup():
    # Body
    body = helpers.get_request_json(request)
    username = body['username']
    password = body['password']
    first_name = body['firstName']
    last_name = body['lastName']

    user_id = user.create_user(username, password, first_name, last_name);

    # Response
    return helpers.send_json_response({ 'UserId': user_id }, 'Usuario creado exitosamente.')


@users.route('/users/login', methods=['POST'])
def login():
    # Body
    body = helpers.get_request_json(request)
    username = body['username']
    password = body['password']

    user_id = user.validate_credentials(username, password)

    # Response
    if user_id == 0:
        return helpers.send_json_response(None, 'Credenciales inválidas.', 'unauthorized', False)
    else:
        return helpers.send_json_response({ 'UserId': user_id })


@users.route('/users/<string:user_id>/profiles', methods=['GET'])
def get_profiles(user_id):
    profiles = user.get_user_profiles(user_id)

    # Response
    return helpers.send_json_response({ 'Profiles': profiles })


@users.route('/users/<string:user_id>/profiles', methods=['POST'])
def create_profile(user_id):
    # Body
    body = helpers.get_request_json(request)
    first_name = body['firstName']
    last_name = body['lastName']

    user_profile_id = user.create_user_profile(user_id, first_name, last_name)

    # Response
    return helpers.send_json_response({ 'UserProfileId': user_profile_id }, 'Perfil creado exitosamente.')
