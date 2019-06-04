
from flask import Flask
import redis

from app.models.base import db
from app.models.douban.movie import Movie
from app.models.douban.star import Star
from app.models.league_of_legends.hero import Hero
from app.models.league_of_legends.skin import Skin
from app.models.league_of_legends.spell import Spell
from app.models.douyu.all import Top120
from app.error.forbid import ForbidException

class RedisFlask(Flask):

    pool = redis.ConnectionPool(host='localhost',port=6379,password='')
    redis = redis.Redis(connection_pool=pool)
    def record(self,ip):
        if not self.redis.get(ip) or self.redis.get(ip).decode(encoding='utf-8') != 'black':
            count = self.redis.incr(ip, 1)
            if count == 1:
                self.redis.expire(ip,600)
            if count>100:
                self._add_black_user(ip)
        else:
            return ForbidException()

    def _add_black_user(self,ip):
        self.redis.set(ip,'black',ex=3600)

def create_app():
    app = RedisFlask(__name__)
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