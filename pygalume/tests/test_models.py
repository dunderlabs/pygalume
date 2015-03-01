from models import Lyrics

from tests import TestBaseDb


class TestLyricsModel(TestBaseDb):

	def test_if_created(self):
		lyrics = self._create()

		expected = [lyrics]
		result = self.session.query(Lyrics).all()
		
		self.assertEqual(result, expected)
