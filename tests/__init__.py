from datetime import datetime
from unittest import TestCase

from pygalume.models import Lyrics
from pygalume.controller import DataBase


class TestBaseDb(TestCase):

    def setUp(self):
        self.__clear_table()
        self.db = DataBase()

    def tearDown(self):
        self.__clear_table()

    def __clear_table(self):
        Lyrics.delete().execute()

    def _create(self, commit=True, **kwargs):
        data = {
            'artist': 'Testudo',
            'artist_url': 'http',
            'music': 'Test',
            'music_url': 'http://',
            'text': 'Testing',
            'translate': 'Testando',
            'artist_tag': 'testudo',
            'music_tag': 'test',
            'created_date': datetime.now().date(),
        }
        data.update(kwargs)

        lyrics = Lyrics(**data)

        if commit:
            lyrics.save()

        return lyrics
