from datetime import datetime

from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

from ..settings import DATABASE_URL


db = SqliteExtDatabase(DATABASE_URL)


class Lyrics(Model):
    '''
        music_tag & artist_tag save the string like this:
        last-kiss & pearl-jam, to improve the search.
    '''

    created_date = DateField(default=datetime.now().date)

    music = CharField(null=False)
    music_tag = CharField(null=False)
    music_url = CharField(null=False)

    text = TextField(null=False)
    translate = TextField()

    artist = CharField(null=False)
    artist_tag = CharField(null=False)
    artist_url = CharField(null=False)

    class Meta:
        database = db
        indexes = (('music', 'artist'), True)

    def __repr__(self):
        return '{0} - {1}'.format(self.artist, self.music)
