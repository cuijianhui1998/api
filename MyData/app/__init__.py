from flask import Flask

from app.models.base import db
from app.models.movie import Movie
from app.models.star import Star


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    register_blueprint(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


#注册蓝图
def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)