from datetime import datetime

from ..models import Lyrics
from .utils import formating_string_name


class DataBase():
    """
        This class will work as a cache.
    """

    def getLyrics(self, artist, music):
        artist_tag = formating_string_name(artist)
        music_tag = formating_string_name(music)

        lyrics = Lyrics.select().where(
            Lyrics.artist_tag == artist_tag,
            Lyrics.music_tag == music_tag
        ).first()

        return lyrics

    def exists(self, artist, music):
        lyrics = self.getLyrics(artist, music)

        if lyrics:
            return True
        else:
            return False

    def getCachedSongs(self):
        lyrics = Lyrics.select().order_by(Lyrics.artist)

        return lyrics
