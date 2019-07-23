from collections import OrderedDict

from app.models.douban.movie import Movie
from app.models.douban.star import Star
from app.error.error_url import NotFoundDataException

def movie_data(movie_type,count):
    '''
    :param movie_type: 传进来的是属于哪一种类,比如正在热映或者top250
    :param start: 从第多少个开始得到
    :param count: 总共需要多少个
    :return: 电影集合,是一个字典
    '''
    result = {
        'total':0,
        'subjects':[]
    }

    movies = Movie.query.filter_by(movie_type=movie_type).limit(count)
    if movies:
        for movie in movies:
            data = OrderedDict()
            actors = Star.query.filter_by(movie_id=movie.movie_id,star_type='actor').all()
            directors = Star.query.filter_by(movie_id=movie.movie_id,star_type='director').all()
            data['影片名'] = movie.title
            data['类型'] = movie.genres
            data['宣传海报'] = movie.poster
            data['收藏数'] = movie.collect_count
            data['原影片名'] = movie.original_title
            data['上映年份'] = movie.pubdate
            data['豆瓣评分'] = movie.score
            data['id'] = movie.movie_id
            data['演员'] = [dict(name=actor.star_name,avatars=actor.avatars,star_id=actor.star_id) for actor in actors] if actors else None
            data['导演'] = [dict(name=director.star_name,avatars=director.avatars,star_id=director.star_id) for director in directors] if directors else None
            result['subjects'].append(data)
        result['total'] = count
        return result
    return NotFoundDataException()
