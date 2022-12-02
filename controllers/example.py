# Dependecies import
from flask import Blueprint, request, jsonify

# Models import
from models import test

# Controller initialization
example = Blueprint('example', __name__)


# Endpoints

@example.route('/example', methods=['GET'])
def get_example():
    try:
        test.verify_connection()
        return {
            'controller': 'Example',
            'method': 'GET'
            }
    except Exception as e:
        return str(e)


@example.route('/example', methods=['POST'])
def post_example():
    return {
        'controller': 'Example',
        'method': 'POST',
        'body': get_request_json(request)
        }


@example.route('/example/<string:id>', methods=['PUT'])
def put_example(id):
    return {
        'controller': 'Example',
        'method': 'PUT',
        'body': get_request_json(request),
        'path': {
            'id': id
            }
        }


@example.route('/example/<string:id>', methods=['PATCH'])
def patch_example(id):
    return {
        'controller': 'Example',
        'method': 'PATCH',
        'body': get_request_json(request),
        'path': {
            'id': id
            }
        }


@example.route('/example/<string:id>', methods=['DELETE'])
def delete_example(id):
    return {
        'controller': 'Example',
        'method': 'DELETE',
        'path': {
            'id': id
            }
        }


# Helpers

def get_request_json(request):
    return request.json if request.is_json else None
