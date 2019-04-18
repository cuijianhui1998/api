from flask import request,Response
import json

from . import web
from app.lib.league import search_hero
from app.error.error_url import LackParamException

@web.route('/v1/game/league')
def hero_info():
    if request.args.get('key'):
        key = request.args.get('key')
        response = search_hero(key)
        return Response(json.dumps(response),mimetype='application/json')
    return LackParamException('key')