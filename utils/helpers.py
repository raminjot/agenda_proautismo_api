# Dependecies import
from flask import json


# Functions

def get_request_json(request): # Object | NULL
    return request.json if request.is_json else None

def get_string_or_default_param(object, key): # String
    try:
        return object[key]
    except KeyError:
        return ''

def send_json_response(data = None, msg = None, code = None, ok = True): # Object
    return {
    'msg': msg,
    'code': code,
    'data': data,
    'ok': ok
    }
