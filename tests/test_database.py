from pygalume.models import Lyrics
from . import TestBaseDb


class TestDataBase(TestBaseDb):

    def test_get_lyrics(self):
        self._create()

        lyrics = self.db.getLyrics(artist='Testudo', music='Test')

        self.assertIsInstance(lyrics, Lyrics)

    def test_if_exist_lyrics(self):
        self._create()

        answer = self.db.exists(artist='Testudo', music='Test')

        self.assertTrue(answer)

    def test_update(self):
        lyrics = self._create()

        another_lyrics = self._create(commit=False, text='Bar')

        self.db.updateLyrics(lyrics, another_lyrics)

        db_lyrics = self.db.getLyrics(artist='Testudo', music='Test')

        self.assertEqual(db_lyrics.text, 'Bar')

    def test_cached_songs(self):
        self._create()
        self._create(artist="test2", music="music2")

        db_lyrics = self.db.getCachedSongs()

        self.assertEqual(len(db_lyrics), 2)
