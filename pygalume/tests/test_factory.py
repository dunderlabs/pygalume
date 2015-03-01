from models import Lyrics
from controller import Factory
from myexceptions import MusicNotFound, ArtistNotFound
from tests import TestBaseDb


class TestFactory(TestBaseDb):

	def test_get_lyrics_with_db(self):
		lyrics = self._create()

		fac = Factory(self.session)

		db_lyrics = fac.getLyrics(artist='Testudo', music='Test')

		self.assertIsInstance(db_lyrics, dict)

	def test_get_lyrics_without_db(self):
		fac = Factory()

		db_lyrics = fac.getLyrics(artist='Pearl Jam', music='Last Kiss')

		self.assertIsInstance(db_lyrics, dict)

	def test_get_lyrics_without_db_error(self):
		fac = Factory()

		with self.assertRaises(ArtistNotFound):
			db_lyrics = fac.getLyrics(artist='Pear', music='Last Kiss')
		
		with self.assertRaises(ArtistNotFound):
			db_lyrics = fac.getLyrics(artist='Pear Jam', music='Last')