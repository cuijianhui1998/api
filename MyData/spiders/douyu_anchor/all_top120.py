import requests,json,csv,time,codecs

from lxml import etree

import sys
sys.path.append(r"D:\ABC\MyData\spiders")
from model.conn import DealData

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

    @classmethod
    def format(cls):
        anchors = cls.get_douyu_data()
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

    def inserts(self,anchors):
        for anchor in anchors:
            self._insert(anchor)

    def truncate(self):
        #清空数据
        self.deal.truncate(table='douyu_top_120')

    def log(self,all_anchors):
        '''
        将每次获取到的数据的前五名记录到文件中,以方便以后分析
        :return:
        '''
        anchors = all_anchors[:5]

        with codecs.open('top5.csv','a+',encoding='utf-8') as f:
            writer = csv.writer(f)

            for index,anchor in enumerate(anchors):
                writer.writerow([int(time.time()),index,anchor['hot'],anchor['anchor_name']])





if __name__ == '__main__':
    douyu = Douyu()
    anchors = douyu.format()
    douyu.truncate()
    douyu.inserts(anchors)
    douyu.log(anchors)




