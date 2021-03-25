from url_manager.url_creator import url_creator_bp
from url_manager.url_handler import url_handler_bp


def route(app):
    app.register_blueprint(url_creator_bp)
    app.register_blueprint(url_handler_bp)

    return True
