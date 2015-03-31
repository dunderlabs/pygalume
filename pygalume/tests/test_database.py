from models import Lyrics

from tests import TestBaseDb


class TestDataBase(TestBaseDb):

	def test_get_lyrics(self):
		self._create()

		lyrics = self.db.getLyrics(artist='Testudo', music='Test')

		self.assertIsInstance(lyrics, Lyrics)

	def test_if_exist_lyrics(self):
		self._create()

		answer = self.db.testIfExist(artist='Testudo', music='Test')

		self.assertTrue(answer)

	def test_add_lyrics(self):
		data = self._create(commit=False)
		lyrics = Lyrics(**data)
		self.db.addLyrics(lyrics)

		result = self.session.query(Lyrics).all()
		self.assertEqual(len(result), 1)