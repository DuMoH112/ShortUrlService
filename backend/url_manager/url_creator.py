from flask import Blueprint, request, jsonify

from app.config import config
from Database.redis import Redis_db

url_creator_bp = Blueprint('url_creator', __name__)


@url_creator_bp.route('/create_short_url', methods=['POST'])
def create_short_url():
    pass
