from werkzeug.exceptions import HTTPException
from flask import request,json

class APIException(HTTPException):
    code = 500
    error_code = 999
    description = '未知错误'

    def __init__(self,code=None,description=None,error_code=None,headers=None):
        if code:
            self.code = code
        if description:
            self.description = description
        if error_code:
            self.error_code = error_code
        super().__init__(None)
    def get_body(self, environ=None):
        body = dict(
            description = self.description,
            error_code = self.error_code,
            request = request.method + ' ' + self.get_url_no_param()
        )
        return json.dumps(body)
    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]

