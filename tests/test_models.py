from pygalume.models import Lyrics

from . import TestBaseDb


class TestLyricsModel(TestBaseDb):

    def test_if_created(self):
        lyrics = self._create()

        expected = [lyrics]
        result = Lyrics.select()

        self.assertEqual(result, expected)

    def test_update(self):
        lyrics = self._create()

        lyrics.text = 'Bar'
        lyrics.save()

        db_lyrics = self.db.getLyrics(artist='Testudo', music='Test')

        self.assertEqual(db_lyrics.text, 'Bar')
