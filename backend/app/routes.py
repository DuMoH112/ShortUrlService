from url_manager.url_creator import url_creator_bp


def route(app):
    app.register_blueprint(url_creator_bp)

    return True
