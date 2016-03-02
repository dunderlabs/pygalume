from datetime import datetime

from pygalume.models import Lyrics
from pygalume.controller import Factory
from pygalume.myexceptions import ArtistNotFound
from . import TestBaseDb


class TestFactory(TestBaseDb):

    def test_get_lyrics_with_db(self):
        ''' When lyrics exists in DB'''
        self._create()

        fac = Factory()

        db_lyrics = fac.getLyrics(artist='Testudo', music='Test')

        self.assertIsInstance(db_lyrics, Lyrics)
        self.assertEqual(str(db_lyrics), 'Testudo - Test')

    def test_get_lyrics_without_db(self):
        ''' When lyrics does not exist in DB '''
        fac = Factory()

        db_lyrics = fac.getLyrics(artist='Pearl Jam', music='Last Kiss')

        self.assertIsInstance(db_lyrics, Lyrics)
        self.assertEqual(str(db_lyrics), 'Pearl Jam - Last Kiss')

    def test_get_expired_lyrics(self):
        ''' When lyrics exists and is expired '''
        fac = Factory()
        old_lyrics = fac.getLyrics(artist='Pearl Jam', music='Last Kiss')

        new_date = datetime.strptime('2014-04-04', '%Y-%m-%d')
        old_lyrics.created_date = new_date

        old_lyrics.save()

        new_lyrics = fac.getLyrics(artist='Pearl Jam', music='Last Kiss')

        expected = datetime.now().date()
        self.assertEqual(new_lyrics.created_date, expected)

    def test_get_lyrics_raises(self):
        fac = Factory()

        with self.assertRaises(ArtistNotFound):
            fac.getLyrics(artist='Pear', music='Last Kiss')

        with self.assertRaises(ArtistNotFound):
            fac.getLyrics(artist='Pear Jam', music='Last')

    def test_get_cached_songs(self):
        ''' When lyrics exists in DB'''
        self._create()
        fac = Factory()

        db_lyrics = fac.getCachedSongs()

        self.assertEqual(len(db_lyrics), 1)
