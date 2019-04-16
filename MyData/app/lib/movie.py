from app.models.movie import Movie
from app.models.star import Star

def movie_data(movie_type,start,count):
    result = {
        'total':count,
        'subjects':[]
    }

    movies = Movie.query.filter_by(movie_type=movie_type).filter(Movie.id>=start).filter(Movie.id<start+count)

    for movie in movies:
        data = {}
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
    return result
