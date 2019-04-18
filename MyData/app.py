import datetime,csv
from app.error.forbid import ForbidException
from flask import request,session

from app import create_app
from app.error.error_url import NotFoundUrlException

app = create_app()

@app.errorhandler(404)
def page_not_found(error):
    return NotFoundUrlException(),404

@app.before_request
def log():
    ip = request.remote_addr
    method = request.method
    args = request.args if request.args else None
    full_path = str(request.full_path)
    url = full_path.split('?')[0]
    time = str(datetime.datetime.now())
    with open('log.csv','a+',encoding='utf-8-sig') as f:
        data = [[ip,method,url,args,time]]
        w = csv.writer(f)
        w.writerows(data)
    if isinstance(app.record(ip),ForbidException):
        return ForbidException()






if __name__ == '__main__':
    app.run(host='localhost',port=10300)
