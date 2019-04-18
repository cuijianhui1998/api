from app.web import web
from flask import request,Response
import json


from app.lib.movie import movie_data

@web.route('/')
def hello():
    return 'hello world'

@web.route('/v1/highscore')
def top250():
    start = 0
    count = 20
    if request.args.get('count'):
        count = request.args.get('count')
    if request.args.get('start'):
        start = request.args.get('start')
    response = movie_data(movie_type='top250',start=start,count=count)
    return Response(json.dumps(response),mimetype='application/json')
