from io import BytesIO
import json,base64

from flask import Response


from . import web
from app.lib.valid_code import ValidateCode

@web.route('/v1/validatecode/<int:width>/<high>')
def hello_world(width,high):
    c = ValidateCode(int(width),int(high))
    res = c.image_init()
    im = res[0]
    code = res[1]
    output = BytesIO()
    im.save(output,'PNG')
    content = 'data:image/png;base64,'+str(base64.b64encode(output.getvalue()),'utf-8')
    response = dict(code=code,content=content)
    return Response(json.dumps(response),mimetype='application/json')