import unittest
from controller import API
from myexceptions import MusicNotFound, ArtistNotFound


class GetLyricsTest(unittest.TestCase):
	def setUp(self):
		self.api = API()

	def test_artist_not_found(self):
		with self.assertRaises(ArtistNotFound):
			self.api.getLyrics('a', 'Last Kiss')

	def test_music_not_found(self):
		with self.assertRaises(MusicNotFound):
			self.api.getLyrics('Pearl Jam', 'LastKiss')
			self.api.getLyrics('Pearl Jam', 'Last--Kiss')

	def test_music_found(self):
		self._test_music('Pearl Jam', 'Last Kiss')

		self._test_music('PearlJam', 'Last Kiss')

		self._test_music('Pearl-Jam', 'Last Kiss')

		self._test_music('Pearl Jam', 'Last-Kiss')

		self._test_music('Pearl Jam', 'Last Kiss ')

		self._test_music('Pearl Jam', ' Last Kiss')

	def _test_music(self, artist, music):
		data = self.api.getLyrics(artist, music)
		self.assertIsInstance(data, dict)
		self.assertIsNotNone(data)
		# 'text' is the key where the lyrics is.
		self.assertIn('text', data.keys())


class GetDiscographyTest(unittest.TestCase):
	def setUp(self):
		self.api = API()

	def test_artist_not_found(self):
		with self.assertRaises(ArtistNotFound):
			self.api.getDiscography('a')
			self.api.getDiscography('PearlJam')

	def test_artist_found(self):
		self._test_artist('Pearl Jam')

		self._test_artist('Pearl Jam ')

		self._test_artist(' Pearl Jam')

		self._test_artist('Pearl-Jam')

	def _test_artist(self, artist):
		data = self.api.getDiscography(artist)
		self.assertIsInstance(data, dict)
		self.assertIsNotNone(data)
		self.assertIn('albums', data.keys())