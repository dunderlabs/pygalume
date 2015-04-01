from datetime import datetime

from sqlalchemy import Column, String, Date, Float, Text, UniqueConstraint
from sqlalchemy.orm import relationship

from .BaseModify import Base


class Lyrics(Base):
	'''
		music_tag & artist_tag save the string like this:
		last-kiss & pearl-jam, to improve the search.
	'''

	created_date = Column(Date, default=datetime.now().date())

	music = Column(String, nullable=False)
	music_tag = Column(String, nullable=False)
	music_url = Column(String, nullable=False)

	text = Column(Text, nullable=False)
	translate = Column(Text)
	
	artist = Column(String, nullable=False)
	artist_tag = Column(String, nullable=False)
	artist_url = Column(String, nullable=False)
	
	__table_args__ = (UniqueConstraint('music', 'artist'),)


	def update(self, new_lyrics):
		self.text = new_lyrics.text
		self.translate = new_lyrics.translate
		self.created_date = datetime.now().date()