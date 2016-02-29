from datetime import datetime, timedelta

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

    def testIfExist(self, artist, music):
        lyrics = self.getLyrics(artist, music)

        if lyrics:
            return True
        else:
            return False

    def addLyrics(self, lyrics):
        lyrics.music_tag = formating_string_name(lyrics.music)
        lyrics.artist_tag = formating_string_name(lyrics.artist)

        lyrics.save()

    def testIfExpired(self, lyrics):
        lyrics_date = lyrics.created_date
        now = datetime.now().date()

        date_to_expires = lyrics_date + timedelta(days=30)

        return date_to_expires < now

    def updateLyrics(self, lyrics, new_lyrics):

        lyrics.text = new_lyrics.text
        lyrics.translate = new_lyrics.translate
        lyrics.created_date = datetime.now().date()

        lyrics.save()

    def getCachedSongs(self):
        lyrics = Lyrics.select()

        return lyrics
