from flask import request,Response
import json

from . import web
from app.lib.anchor import get_top120

@web.route('/v1/douyu/top120')
def douyu_top120():
    start = request.args.get('start',default=0)
    count = request.args.get('count',default=20)
    response = get_top120(start,count)
    return Response(json.dumps(response), mimetype='application/json')
