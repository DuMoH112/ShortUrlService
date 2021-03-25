from flask import Blueprint, jsonify, redirect

from Database.redis import Redis_db

url_handler_bp = Blueprint('url_handler', __name__)


@url_handler_bp.route('/get_full_url/<string:short_url>', methods=['GET'])
def get_full_url(short_url):

    redis = Redis_db()
    lng_url = redis.hm_select_data(short_url, "long_url")

    redis.close_connection()

    if lng_url:
        return jsonify(lng_url[0])

    return jsonify("Not Found"), 404


@url_handler_bp.route('/<string:short_url>', methods=['GET'])
def url_handler(short_url):

    redis = Redis_db()
    lng_url = redis.hm_select_data(short_url, "long_url")

    redis.close_connection()
    if lng_url:
        return redirect(lng_url[0])

    return jsonify("Not Found"), 404
