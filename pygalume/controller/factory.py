from .database import DataBase
from .api import API


class Factory():

    def __init__(self):
        self._db = DataBase()
        self._api = API()

    def getLyrics(self, artist, music):

        try:
            if self._db.exists(artist, music):
                lyrics = self._db.getLyrics(artist, music)

                if lyrics.expired():
                    new_lyrics = self._api.getLyrics(artist, music)
                    lyrics.updateTo(new_lyrics)

            else:
                lyrics = self._api.getLyrics(artist, music)
                lyrics.save()
        except:
            raise

        return lyrics

    def getDiscography(self, artist):

        try:
            return self._api.getDiscography(artist)

        except:
            raise

    def getSongs(self, artist, album):

        try:
            return self._api.getSongs(artist, album)

        except:
            raise

    def getCachedSongs(self):

        try:
            return self._db.getCachedSongs()
        except:
            raise
