from datetime import datetime, timedelta

from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

from ..settings import DATABASE_URL
from ..controller.utils import formating_string_name

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

    def save(self, *args, **kwargs):
        self.music_tag = formating_string_name(self.music)
        self.artist_tag = formating_string_name(self.artist)

        return super(Lyrics, self).save(*args, **kwargs)

    class Meta:
        database = db
        indexes = (('music', 'artist'), True)

    def __repr__(self):
        return '{0} - {1}'.format(self.artist, self.music)

    def expired(self):
        lyrics_date = self.created_date
        now = datetime.now().date()

        date_to_expires = lyrics_date + timedelta(days=30)

        return date_to_expires < now
