from sqlalchemy import and_

from myexceptions import MusicNotFound, ArtistNotFound
from models import Lyrics, session as s
from .utils import formating_string_name


class DataBase():
	'''
		This class will work as a cache.
	'''

	def __init__(self, session=s):
		self.session = session

	def getLyrics(self, artist, music):
		artist_tag = formating_string_name(artist)
		music_tag = formating_string_name(music)
		
		lyrics = self.session.query(Lyrics).\
				filter(and_(Lyrics.music_tag == music_tag, Lyrics.artist_tag == artist_tag)).\
				first()

		return lyrics

	def searchLyrics(self, artist, music):
		artist_tag = formating_string_name(artist)
		music_tag = formating_string_name(music)

		music = self.session.query(Lyrics).filter(Lyrics.music_tag == music_tag).first()
		artist = self.session.query(Lyrics).filter(Lyrics.artist_tag == artist_tag).first()

		if artist and music:
			return True
		else:
			return False

	def addLyrics(self, data):
		lyrics = Lyrics(**data)
		lyrics.music_tag = formating_string_name(lyrics.music)
		lyrics.artist_tag = formating_string_name(lyrics.artist)
		
		self.session.add(lyrics)
		self.session.commit()
