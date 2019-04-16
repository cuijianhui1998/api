import requests,json
from queue import Queue
from threading import Thread

from spiders.model.util import DealData




def myspider(url):
    deal_data = DealData()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    response = requests.get(url=url,headers=headers)
    result = json.loads(response.text)
    for data in result['subjects']:
        genres = ','.join(data['genres'])
        title = data['title']
        collect_count = data['collect_count']
        original_title = data['original_title']
        pubdate = data['year']
        movie_id = data['id']
        poster = data['images']['small']
        score = data['rating']['average']
        deal_data.top250(genres=genres,title=title,collect_count=collect_count,original_title=original_title,
                    pubdate=pubdate,movie_id=movie_id,poster=poster,score=score)

        for star in data['casts']:
            name = star['name']
            try:
                avatars = star['avatars']['small']
            except TypeError:
                avatars = '未知'
            star_id = star['id']
            deal_data.stars(star_name=name,avatars=avatars,star_id=star_id,movie_id=movie_id,star_type='actor')
        for star in data['directors']:
            name = star['name']
            try:
                avatars = star['avatars']['small']
            except TypeError:
                avatars = '未知'
            star_id = star['id']
            deal_data.stars(star_name=name,avatars=avatars,star_id=star_id,movie_id=movie_id,star_type='director')



if __name__ == '__main__':
    spider_url = Queue()
    for i in range(1, 13):
        start = (i - 1) * 20
        spider_url.put(
            'http://api.douban.com/v2/movie/top250?start={start}&count={count}'.format(start=start, count=20))
    spider_url.put('http://api.douban.com/v2/movie/top250?start=240&count=10')

    while not spider_url.empty():
        # for _ in range(5):
        url = spider_url.get()
        print(url)
        thread1 = Thread(target=myspider,args=(url,))
        thread1.start()
    db = DealData()
    db.close()
    print('完成了')
