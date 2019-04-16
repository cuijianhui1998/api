from sqlalchemy import Column,Integer,String,ForeignKey

from app.models.base import Base
from app.models.movie import Movie

class Star(Base):
    __tablename__ = 'star'
    id = Column(Integer,autoincrement=True,primary_key=True)
    star_name = Column(String(20))
    avatars = Column(String(200))
    movie_id = Column(String(20),ForeignKey(Movie.movie_id))
    star_id = Column(String(20),unique=True)
    star_type = Column(String(10))



