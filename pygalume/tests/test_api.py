import unittest

from models import Lyrics
from controller import API
from myexceptions import MusicNotFound, ArtistNotFound, DiscographyNotFound


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
        lyrics = self.api.getLyrics(artist, music)

        self.assertIsInstance(lyrics, Lyrics)

        self.assertEqual(lyrics.music, 'Last Kiss')
        self.assertEqual(lyrics.artist, 'Pearl Jam')


class GetDiscographyTest(unittest.TestCase):
    def setUp(self):
        self.api = API()

    def test_artist_not_found(self):
        with self.assertRaises(ArtistNotFound):
            self.api.getDiscography('a')
            self.api.getDiscography('PearlJam')
            self.api.getDiscography('Pearl Ja')

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


class GetSongsTest(unittest.TestCase):

    def setUp(self):
        self.api = API()

    def test_artist_not_found(self):
        with self.assertRaises(ArtistNotFound):
            self.api.getSongs('Pearl Ja', 'Ten')

    def test_discography_not_found(self):
        with self.assertRaises(DiscographyNotFound):
            self.api.getSongs('Pearl Jam', 'Aasd')
            self.api.getSongs('PearlJam', 'Kiss')
            self.api.getSongs('Pearl-Jam', 'Last')

    def test_song_found(self):
        result = self.api.getSongs('Pearl Jam', 'No Code')
        self.assertIsInstance(result, list)
        self.assertNotEqual(result[0], None)

        result = self.api.getSongs('Pearl-Jam', 'No Code')
        self.assertIsInstance(result, list)
        self.assertNotEqual(result[0], None)
