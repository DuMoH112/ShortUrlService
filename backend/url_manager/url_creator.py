import uuid
import hashlib

from flask import Blueprint, request, jsonify

from app.config import config
from Database.redis import Redis_db

url_creator_bp = Blueprint('url_creator', __name__)


@url_creator_bp.route('/create_short_url', methods=['POST'])
def create_short_url():
    json = request.get_json(silent=True)
    if not json:
        return jsonify({"message": "JSON не найден"}), 204

    long_url = json.get('long_url')
    if not long_url:
        return jsonify({"message": "Поле long_url не найдено"}), 204

    domain = config['APP']['URL_SERVICE']

    salt = uuid.uuid4().hex
    hash_url = hashlib.pbkdf2_hmac(
        'sha256', long_url.encode('utf-8'),
        salt.encode('utf-8'), 2, dklen=6
    )
    link_id = hash_url.hex()

    redis = Redis_db()

    redis.hm_insert_data(
        link_id,
        {
            "long_url": str(long_url),
            "salt": str(salt)
        }
    )

    redis.close_connection()
    return jsonify(f'http://{domain}/{link_id}')
