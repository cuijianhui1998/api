from flask import current_app
from . import web


@web.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('static/favicon.ico')

