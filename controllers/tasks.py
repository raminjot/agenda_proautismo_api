# Dependecies import
from flask import Blueprint, request, jsonify, json

# Controller initialization
tasks = Blueprint('tasks', __name__)


class task:
    def __init__(self, id, name, img_url):
        self.id = id
        self.name = name 
        self.img_url = img_url

class task_option:
    def __init__(self, id, img_url):
        self.id = id
        self.img_url = img_url


# Endpoints

@tasks.route('/tasks', methods=['GET'])
def get_tasks():

    # TODO Obtener la lista de tareas/actividades de la BD a desplegar en la app.

    task_list = []

    task_list.append((task(1, 'Tender la cama', 'https://i.pinimg.com/originals/35/85/2a/35852ae56097fda9bc4517590a912530.jpg').__dict__))
    task_list.append((task(2, 'Lavarse los dientes', 'http://www.hospitaldefuenlabrada.org/TEA/img/pictos/cepillar-dientes.jpg').__dict__))
    task_list.append((task(3, 'Hacer la mesa', 'https://educasaac.educa.madrid.org/uploads/image.php?file=201702091514452.png&name=poner-la-mesa_picto_color&folder=images').__dict__))

    return send_json_response(task_list)

@tasks.route('/tasks/<string:task_id>/start', methods=['POST'])
def start_task(task_id):

    json = get_request_json(request)

    user_id = json['userId']

    # TODO Inicializar una sesión para la actividad y guardar el registro de elecciones en BD.
    # Si el usuario tiene una actividad sin completar (por si abandona la app), marcar como completadas la(s) tarea(s) incompletas.

    session_id = 33;

    return send_json_response(session_id)


@tasks.route('/tasks/<string:session_id>', methods=['GET'])
def get_task_options(session_id):

    # TODO Obtener la lista de tareas/actividades de la BD a desplegar en la app.

    task_list = []

    task_list.append((task_option(1, 'https://i.pinimg.com/originals/35/85/2a/35852ae56097fda9bc4517590a912530.jpg').__dict__))
    task_list.append((task_option(2, 'http://www.hospitaldefuenlabrada.org/TEA/img/pictos/cepillar-dientes.jpg').__dict__))
    task_list.append((task_option(3, 'https://educasaac.educa.madrid.org/uploads/image.php?file=201702091514452.png&name=poner-la-mesa_picto_color&folder=images').__dict__))

    return send_json_response(task_list)


@tasks.route('/tasks/<string:task_id>/finish', methods=['POST'])
def finish_task(task_id):

    # TODO Finalizar la sesión de la actividad en BD.

    return send_json_response()


# Helpers

def get_request_json(request):
    return request.json if request.is_json else None

def send_json_response(data = None, msg = None, code = None, ok = True):
    return {
    'msg': msg,
    'code': code,
    'data': data,
    'ok': ok
    }
