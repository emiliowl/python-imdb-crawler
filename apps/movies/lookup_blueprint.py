from logging import info
from flask import Blueprint, request, jsonify
from apps.movies.services import search_in_index,director_index, stars_index, load


bp = Blueprint('movies', __name__)


def init():
    info('initializing lookup_blueprint...')
    load()


@bp.route('/healthcheck')
def healthcheck():
    return 'movies lookup API up and running ...'


@bp.route('/search', methods=['get'])
def index():
    criteria = request.args.get('criteria', '')

    criterias = criteria.split(' ')
    criteria_list = list(map(lambda el: el.strip(),criterias))

    result_list_directors = []
    result_list_stars = []
    for criteria in criteria_list:
        directors_result = search_in_index(criteria, director_index)
        result_list_directors += list(map(lambda movie: movie["title"] ,directors_result))

    for criteria in criteria_list:
        stars_result = search_in_index(criteria, stars_index)
        result_list_stars += list(map(lambda movie: movie["title"] ,stars_result))

    if len(result_list_directors) and len(result_list_stars):
        response = list(set.intersection(set(result_list_directors), set(result_list_stars)))
    elif len(result_list_directors):
        response = result_list_directors
    elif len(result_list_stars):
        response = result_list_stars

    return jsonify(response)
