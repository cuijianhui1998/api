from app.error.base import APIException

class LackParamException(APIException):
    code = 404
    error_code = 10005
    def __init__(self,param):
        self.description = '缺少参数 {}'.format(param)
        super().__init__(None)

class NotFoundUrlException(APIException):
    code = 404
    error_code = 10006
    description = '你来到了未知区域'

class NotFoundDataException(APIException):
    code = 404
    error_code = 100007
    description = '你请求的资源暂时还没有,我们正在努力获取中.....'

