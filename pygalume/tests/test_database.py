from models import Lyrics

from tests import TestBaseDb


class TestDataBase(TestBaseDb):

	def test_get_lyrics(self):
		self._create()

		lyrics = self.db.getLyrics(artist='Testudo', music='Test')

		self.assertIsInstance(lyrics, Lyrics)

	def test_search_lyrics(self):
		self._create()

		answer = self.db.searchLyrics(artist='Testudo', music='Test')

		self.assertTrue(answer)

	def test_add_lyrics(self):
		data = self._create(commit=False)

		self.db.addLyrics(data)

		result = self.session.query(Lyrics).all()
		self.assertEqual(len(result), 1)