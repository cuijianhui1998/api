from sqlalchemy import Column,String

from app.models.base import Base

class Skin(Base):
    __tablename__ = 'hero_skins'
    skin_id = Column(String(10),primary_key=True)
    skin_name = Column(String(20))
    skin_image = Column(String(150))