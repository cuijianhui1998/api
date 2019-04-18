from sqlalchemy import Column,Integer,String,Text

from app.models.base import Base

class Hero(Base):
    __tablename__ = 'hero'
    id = Column(Integer,primary_key=True,autoincrement=True)
    url = Column(String(100))
    hero_name = Column(String(30))
    title = Column(String(20))
    tags = Column(String(50))
    skins_count = Column(String(5))
    info = Column(String(20))
    lore = Column(Text)
    allytips = Column(String(500))
    enemytips = Column(String(500))