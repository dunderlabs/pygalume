from datetime import datetime

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

        another_lyrics = self._create(commit=False, text='Bar')

        lyrics.updateTo(another_lyrics)

        db_lyrics = self.db.getLyrics(artist='Testudo', music='Test')

        self.assertEqual(db_lyrics.text, 'Bar')

    def test_expired(self):
        new_date = datetime.strptime('2014-04-04', '%Y-%m-%d').date()
        lyrics = self._create(created_date=new_date)

        answer = lyrics.expired()

        self.assertTrue(answer)

    def test_not_expired(self):
        lyrics = self._create()

        answer = lyrics.expired()

        self.assertFalse(answer)
