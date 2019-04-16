import pymysql,requests

class DealData:
    def __init__(self):
        self.db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            db='spider',
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.db.cursor()

    def top250(self,**kwargs):
        movie_id = kwargs['movie_id']
        genres = kwargs['genres']
        title = kwargs['title']
        collect_count = kwargs['collect_count']
        original_title = kwargs['original_title']
        pubdate = kwargs['pubdate']
        score = kwargs['score']
        poster = kwargs['poster']
        print(title)
        self.download_movie_image(movie_id,poster)
        sql = 'insert into movie(genres,title,poster,collect_count,original_title,pubdate,score,movie_id,movie_type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s) '
        self.cursor.execute(sql, (genres,title,poster,collect_count,original_title,pubdate,score,movie_id,'top250'))
        self.db.commit()

    def stars(self,**kwargs):
        search_sql = "select star_id from star where star_id=%s"
        self.cursor.execute(search_sql, kwargs['star_id'])
        if not self.cursor.fetchone():
            star_name = kwargs['star_name']
            avatars = kwargs['avatars']
            movie_id = kwargs['movie_id']
            star_id = kwargs['star_id']
            star_type = kwargs['star_type']
            print(star_name)
            self.download_star_image(star_id,avatars)
            sql = 'insert into star(star_name,avatars,movie_id,star_id,star_type) values(%s,%s,%s,%s,%s) '
            self.cursor.execute(sql, (star_name,avatars,movie_id,star_id,star_type))
            self.db.commit()


    def download_movie_image(self,id,poster):
        with open('D:\BookImages\movie\{}.jpg'.format(id),'wb') as f:
            result = requests.get(poster)
            f.write(result.content)

    def download_star_image(self,id,avatars):
        with open('D:\BookImages\star\{}.jpg'.format(id), 'wb') as f:
            result = requests.get(avatars)
            f.write(result.content)
    def close(self):
        self.cursor.close()
        self.db.close()
