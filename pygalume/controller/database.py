from datetime import datetime, timedelta

from sqlalchemy import and_

# from myexceptions import MusicNotFound, ArtistNotFound
from models import Lyrics, session as s
from .utils import formating_string_name


class DataBase():
    """
        This class will work as a cache.
    """

    def __init__(self, session=s):
        self.session = session

    def getLyrics(self, artist, music):
        artist_tag = formating_string_name(artist)
        music_tag = formating_string_name(music)

        lyrics = self.session.query(Lyrics).filter(
            and_(
                Lyrics.music_tag == music_tag, Lyrics.artist_tag == artist_tag
            )).first()

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

        self.session.add(lyrics)
        self.session.commit()

    def testIfExpired(self, lyrics):
        lyrics_date = lyrics.created_date
        now = datetime.now().date()

        date_to_expires = lyrics_date + timedelta(days=30)

        return date_to_expires < now

    def updateLyrics(self, lyrics, new_lyrics):
        lyrics.update(new_lyrics)

        self.session.commit()

    def getCachedSongs(self):
        lyrics = self.session.query(Lyrics).all()
        return lyrics
