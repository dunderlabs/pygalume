from sqlalchemy import Column, String, Date, Float, Text, UniqueConstraint
from sqlalchemy.orm import relationship

from .BaseModify import Base


class Lyrics(Base):
	'''
		music_tag & artist_tag save the string like this:
		last-kiss & pearl-jam, to improve the search.
	'''
	music = Column(String, nullable=False)
	music_tag = Column(String, nullable=False)
	music_url = Column(String, nullable=False)

	text = Column(Text, nullable=False)
	translate = Column(Text)
	
	artist = Column(String, nullable=False)
	artist_tag = Column(String, nullable=False)
	artist_url = Column(String, nullable=False)
	
	__table_args__ = (UniqueConstraint('music', 'artist'),)
