from sqlalchemy import Column, ForeignKey, String, true
from models.base import Base
from sqlalchemy.orm import relationship


class Favorite(Base):
    __tablename__ = 'favorites'

    id = Column(String(100) ,primary_key=true)
    song_id = Column(String(100), ForeignKey("songs.id"))
    user_id = Column(String(100), ForeignKey("users.id"))

    song = relationship('Song')
    user = relationship('User',back_populates='favorites')

