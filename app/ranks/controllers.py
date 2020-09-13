from flask import Blueprint, jsonify, request

from app.utils.constants import HTTP_200_OK, HTTP_201_CREATED
from app.utils.dbConnections import get_mysql_connection, close_mysql_connection
from .services import get_rank, get_ranks_list, update_new_score

ranks_module = Blueprint('ranks', __name__, url_prefix='/ranks')


@ranks_module.route('/get-rank', methods=['GET'])
def get_user_rank():
    request_data = request.args
    user_id = request_data.get('user_id')
    mysql_conn = get_mysql_connection()
    status, rank = get_rank(mysql_conn, user_id)
    close_mysql_connection(mysql_conn)
    response_data = {
        'data': {
            'rank': rank,
            'status': status
        }
    }

    return jsonify(response_data), HTTP_200_OK


@ranks_module.route('/ranks-list', methods=['GET'])
def get_user_ranks_list():
    request_data = request.args
    n = request_data.get('n')
    mysql_conn = get_mysql_connection()
    ranks_list = get_ranks_list(mysql_conn, n)
    close_mysql_connection(mysql_conn)
    response_data = {
        'data': {
            'rank_list': ranks_list
        }
    }

    return jsonify(response_data), HTTP_200_OK


@ranks_module.route('/update-score', methods=['POST'])
def update_user_score():
    print(request.args)
    request_data = request.get_json()
    user_id = request_data.get('user_id')
    score = request_data.get('score')
    mysql_conn = get_mysql_connection()
    new_rank = update_new_score(mysql_conn, user_id, score)
    close_mysql_connection(mysql_conn)
    response_data = {
        'data': {
            'status': 'success',
            'rank': new_rank
        }
    }

    return jsonify(response_data), HTTP_201_CREATED
