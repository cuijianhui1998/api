from flask import request,Response
import json

from . import web
from app.lib.anchor import get_top120

@web.route('/v1/douyu/top120')
def douyu_top120():
    count = 20
    start = 0
    if request.args.get('count'):
        count = int(request.args.get('count', 0))
    if request.args.get('start'):
        start = int(request.args.get('start', 20))
    response = get_top120(start,count)
    return Response(json.dumps(response), mimetype='application/json')
