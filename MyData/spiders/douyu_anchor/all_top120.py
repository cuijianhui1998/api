import requests,json,pprint
from dataclasses import dataclass

from lxml import etree
import pymysql

from spiders.model.conn import DealData

class Douyu:
    def __init__(self):
        self.deal = DealData()

    @staticmethod
    def get_douyu_data():
        response = requests.get('https://www.douyu.com/directory/all')
        html = etree.HTML(response.text)

        data = html.xpath('//script[2]/text()')
        a = data[0].replace('var $DATA = ','').replace(";\n        var pageType = \'all\';",'')
        dicts = json.loads(a)
        return dicts['list']


    def format(self):
        anchors = self.get_douyu_data()
        anchor_list = []
        for anchor in anchors:
            anchor_list.append(
                {'anchor_type':anchor['c2name'],
                 'anchor_name':anchor['nn'],
                 'od':anchor['od'],
                 'hot':anchor['ol'],
                 'room_id':anchor['rid'],
                 'room_name':anchor['rn'],
                 'room_url':anchor['url'],
                 'anchor_id':anchor['uid']
                 })
        return anchor_list

    def _insert(self,anchor):
        #插入每天的数据
        column = list(anchor.keys())
        keys = list(anchor.values())
        self.deal.insert(column,*keys,table='douyu_top_120')

    def inserts(self):
        for anchor in self.format():
            self._insert(anchor)

    def truncate(self):
        #清空数据
        self.deal.truncate(table='douyu_top_120')

if __name__ == '__main__':
    douyu = Douyu()
    douyu.truncate()
    douyu.inserts()




