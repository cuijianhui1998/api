from sqlalchemy import Column,String

from app.models.base import Base

class Spell(Base):
    __tablename__ = 'hero_spells'
    id = Column(String(5),primary_key=True)
    hero_name = Column(String(10))
    passive_name = Column(String(15))
    passive_image = Column(String(150))
    Q_name = Column(String(15))
    Q_image = Column(String(150))
    W_name = Column(String(15))
    W_image = Column(String(150))
    E_name = Column(String(15))
    E_image = Column(String(150))
    R_name = Column(String(15))
    R_image = Column(String(150))