from dataclasses import dataclass

from sqlalchemy import desc

from app.models.douyu.all import Top120
from app.error.error_url import NotFoundDataException

@dataclass()
class _Myclass():
    anchor_type:str
    anchor_name:str
    od:str
    hot:int
    room_id:int
    room_name:str
    room_url:str
    anchor_id:int

def get_top120(start,count):
    if start+count>120:
        raise NotFoundDataException()
    total = count
    anchors = {'types':'DouYu','total':count,'content':[]}
    all_anchor = []
    datas = Top120.query.order_by(Top120.hot.desc()).all()
    for data in datas:
        result = {}
        result['room_id'] = data.room_id
        result['anchor_name'] = data.anchor_name
        result['anchor_type'] = data.anchor_type
        result['room_name'] = data.room_name
        result['od'] = data.od
        result['hot'] = data.hot
        result['url'] = 'https://www.douyu.com{}'.format(data.room_url)
        result['anchor_id'] = data.anchor_id
        all_anchor.append(result)
    anchors['content'] = all_anchor[start:start+count]
    return anchors