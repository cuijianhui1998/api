from app.web import web
from flask import request,Response,jsonify
import json


from app.lib.movie import movie_data

@web.route('/')
def hello():
    return 'hello world'

@web.route('/v1/highscore/')
def top250():
    count=20
    if request.args.get('count'):
        count = int(request.args.get('count'))
    response = movie_data(movie_type='top250',count=count)
    return Response(json.dumps(response),mimetype='application/json')