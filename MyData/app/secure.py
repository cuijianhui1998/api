import redis
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/spider?charset=utf8'
SECRET_KEY = '2dh3erj3khf23kjk2'


SESSION_TYPE = 'redis'
SESSION_REDIS = redis.Redis(host='localhost', port='6379', password='')
SESSION_KEY_PREFIX = 'flask'