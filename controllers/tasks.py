# Dependecies import
from flask import Blueprint, request

# Models import
from models import activity
from models import task_node
from models import task
from models import user_profile

# Utils import
from utils import helpers

# Modules import
import os

# Controller initialization
tasks = Blueprint('tasks', __name__)


# Endpoints

@tasks.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = task.get_all()

    # Response
    return helpers.send_json_response({ 'Tasks': task_list })


@tasks.route('/tasks/start', methods=['POST'])
def start_task():
    # Body
    body = helpers.get_request_json(request)

    # Task Validation

    task_id = helpers.get_number_or_default_param(body, 'taskId')

    task_selected = task.get_single_by_task_id(task_id)

    if task_selected == None:
        return helpers.send_json_response(None, 'Tarea no encontrada.', 'bad_request', False)

    # User Profile Validation

    user_profile_id = helpers.get_number_or_default_param(body, 'userProfileId')

    user_profile_id_exists = user_profile.validate_existing_user_profile_id(user_profile_id)

    if user_profile_id_exists == False:
        return helpers.send_json_response(None, 'Perfil no encontrado.', 'bad_request', False)

    activity.finish_user_profile_activities(user_profile_id)

    activity_id = activity.create_activity(user_profile_id, task_selected)

    # Response
    return helpers.send_json_response({ 'ActivityId': activity_id })


@tasks.route('/tasks/<string:activity_id>', methods=['GET'])
def get_task_options(activity_id):
    # Body
    body = helpers.get_request_json(request)

    current_activity = activity.get_single_by_activity_id(activity_id);

    if current_activity == None:
        return helpers.send_json_response(None, 'Actividad no encontrada.', 'bad_request', False)

    task_node_id = helpers.get_number_or_default_param(body, 'selectedOption')

    if task_node_id == 0:
        activity.set_activity_start(activity_id)
        task_node_id = task_node.get_first_task_node_id(current_activity['TaskId'])
    else:
        task_node_name = task_node.get_task_node_name(task_node_id)
        activity.update_activity_result(activity_id, task_node_name)

    options = task_node.get_child_nodes(task_node_id)

    if options:

        for option in options:
            option['TaskNodeImage'] = os.getenv('URL_BLOB') + '/assets/images/tasks-nodes/' + str(option['TaskNodeId']) + '.png'

        return helpers.send_json_response({ 'Options': options })
    else:
        activity.set_activity_end(activity_id)
        return helpers.send_json_response(None, 'Actividad finalizada')


@tasks.route('/tasks/finish', methods=['POST'])
def finish_task():
    # Body
    body = helpers.get_request_json(request)

    activity_id = helpers.get_number_or_default_param(body, 'activityId')

    activity_to_end = activity.get_single_by_activity_id(activity_id);

    if activity_to_end == None:
        return helpers.send_json_response(None, 'Actividad no encontrada.', 'bad_request', False)

    if activity_to_end['ActivityStatus'] == 1:
        activity.set_activity_end(activity_id)

    return helpers.send_json_response()
