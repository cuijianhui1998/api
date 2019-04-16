from sqlalchemy import Column,String,Integer

from app.models.base import Base

class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer,autoincrement=True,primary_key=True)
    genres = Column(String(20))
    title = Column(String(30))
    poster = Column(String(100))
    collect_count = Column(String(20))
    original_title = Column(String(50))
    pubdate = Column(String(8))
    score = Column(String(8))
    movie_id = Column(String(10),unique=True)
    movie_type = Column(String(20))

