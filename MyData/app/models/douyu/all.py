from sqlalchemy import Column,String,Integer

from app.models.base import Base


class Top120(Base):
    __tablename__ = 'douyu_top_120'
    id = Column(Integer,primary_key=True,autoincrement=True)
    room_id = Column(Integer)
    anchor_name = Column(String(50))
    anchor_type = Column(String(50))
    room_name = Column(String(50))
    od = Column(String(50))
    hot = Column(Integer)
    room_url = Column(String(100))
    anchor_id = Column(Integer)