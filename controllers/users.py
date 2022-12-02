# Dependecies import
from flask import Blueprint, request, jsonify, json

# Models import
from models import user
from models import user_profile

# Utils import
from utils import helpers

# Controller initialization
users = Blueprint('users', __name__)


# Endpoints

@users.route('/users/sign_up', methods=['POST'])
def signup():
    # Body
    body = helpers.get_request_json(request)

    username = helpers.get_string_or_default_param(body, 'username')
    password = helpers.get_string_or_default_param(body, 'password')
    first_name = helpers.get_string_or_default_param(body, 'first_name')
    last_name = helpers.get_string_or_default_param(body, 'last_name')

    username_exists = user.validate_existing_username(username)

    if username_exists == True:
        return helpers.send_json_response(None, 'El nombre de usuario ya existe.', 'conflict', False)

    user_id = user.create_user(username, password, first_name, last_name)

    # Response
    return helpers.send_json_response({ 'UserId': user_id }, 'Usuario creado exitosamente.')


@users.route('/users/login', methods=['POST'])
def login():
    # Body
    body = helpers.get_request_json(request)

    username = helpers.get_string_or_default_param(body, 'username')
    password = helpers.get_string_or_default_param(body, 'password')

    user_id = user.validate_credentials(username, password)

    # Response
    if user_id == 0:
        return helpers.send_json_response(None, 'Credenciales inválidas.', 'unauthorized', False)
    else:
        return helpers.send_json_response({ 'UserId': user_id })


@users.route('/users/<string:user_id>/profiles', methods=['GET'])
def get_profiles(user_id):
    profiles = user_profile.get_user_profiles(user_id)

    # Response
    return helpers.send_json_response({ 'Profiles': profiles })


@users.route('/users/<string:user_id>/profiles', methods=['POST'])
def create_profile(user_id):
    # Body
    body = helpers.get_request_json(request)

    user_id_exists = user.validate_existing_user_id(user_id)

    if user_id_exists == False:
        return helpers.send_json_response(None, 'Usuario no encontrado.', 'bad_request', False)

    first_name = helpers.get_string_or_default_param(body, 'firstName')
    last_name = helpers.get_string_or_default_param(body, 'lastName')

    user_profile_id = user_profile.create_user_profile(user_id, first_name, last_name)

    # Response
    return helpers.send_json_response({ 'UserProfileId': user_profile_id }, 'Perfil creado exitosamente.')
