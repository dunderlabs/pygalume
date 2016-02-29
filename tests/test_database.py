from datetime import datetime

from pygalume.models import Lyrics
from . import TestBaseDb


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
        lyrics = self._create(commit=False)
        self.db.addLyrics(lyrics)

        result = Lyrics.select()
        self.assertEqual(len(result), 1)

    def test_expired(self):
        new_date = datetime.strptime('2014-04-04', '%Y-%m-%d').date()
        lyrics = self._create(created_date=new_date)

        answer = self.db.testIfExpired(lyrics)

        self.assertTrue(answer)

    def test_not_expired(self):
        lyrics = self._create()

        answer = self.db.testIfExpired(lyrics)

        self.assertFalse(answer)

    def test_update(self):
        lyrics = self._create()

        another_lyrics = self._create(commit=False, text='Bar')

        self.db.updateLyrics(lyrics, another_lyrics)

        db_lyrics = self.db.getLyrics(artist='Testudo', music='Test')

        self.assertEqual(db_lyrics.text, 'Bar')

    def test_cached_songs(self):
        lyrics = self._create()
        lyrics = self._create(artist="test2", music="music2")

        db_lyrics = self.db.getCachedSongs()

        self.assertEqual(len(db_lyrics), 2)
