from sqlalchemy import TEXT, VARCHAR, Column, String
from models.base import Base


class Song(Base):
    __tablename__ ='songs'
    id = Column(String(100), primary_key=True)
    song_url = Column(TEXT(200))
    thumbnail_url = Column(TEXT(200))
    artist = Column(TEXT(50))
    song_name = Column(VARCHAR(100))
    hex_code = Column(VARCHAR(6)) 
