from .database import DataBase
from .api import API

class Factory():

	def __init__(self, session=None):
		self.session = session
		
		if self.session:
			self._db = DataBase(self.session)
		else:
			self._db = DataBase()
		
		self._api = API()

	def getLyrics(self, artist, music):

		try:
			if self._db.searchLyrics(artist, music):
				lyrics = self._db.getLyrics(artist, music)

			else:
				lyrics = self._api.getLyrics(artist, music)
				self._db.addLyrics(lyrics)
		except:
			raise

		return lyrics

	def getDiscography(self, artist):

		try:
			return self._api.getDiscography(artist)
			
		except:
			raise
