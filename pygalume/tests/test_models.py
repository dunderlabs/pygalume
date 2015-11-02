from models import Lyrics

from tests import TestBaseDb


class TestLyricsModel(TestBaseDb):

    def test_if_created(self):
        lyrics = self._create()

        expected = [lyrics]
        result = self.session.query(Lyrics).all()

        self.assertEqual(result, expected)

    def test_update(self):
        lyrics = self._create()

        another_lyrics = self._create(commit=False, text='Bar')

        lyrics.update(another_lyrics)

        db_lyrics = self.db.getLyrics(artist='Testudo', music='Test')

        self.assertEqual(db_lyrics.text, 'Bar')
