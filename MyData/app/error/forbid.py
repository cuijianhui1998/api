from app.error.base import APIException

class ForbidException(APIException):
    code = 403
    error_code = 10012
    description = '403 forbidden'