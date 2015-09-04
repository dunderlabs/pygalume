import requests as r
from settings import API_URL
from models import Lyrics
from myexceptions import MusicNotFound, ArtistNotFound, DiscographyNotFound

from .utils import formating_string_name


SONG_NOT_FOUND = 'song_notfound'
NOT_FOUND = 'notfound'


class API():

    def getLyrics(self, artist, music):
        artist = formating_string_name(artist)
        music = formating_string_name(music)

        response = r.get('{0}art={1}&mus={2}'.format(API_URL, artist, music))
        response = response.json()

        if response['type'] == SONG_NOT_FOUND:
            raise MusicNotFound

        elif response['type'] == NOT_FOUND:
            raise ArtistNotFound

        else:
            # If the song is in portuguese, for example
            # there is no translation.
            try:
                translate = response['mus'][0]['translate']
                translate = translate[0]['text']
            except KeyError:
                translate = ''

            data = {
                'artist': response['art']['name'],
                'artist_url': response['art']['url'],
                'music': response['mus'][0]['name'],
                'music_url': response['mus'][0]['url'],
                'text': response['mus'][0]['text'],
                'translate': translate,
            }
            return Lyrics(**data)

    def getDiscography(self, artist):
        artist = formating_string_name(artist)
        response = r.get('http://www.vagalume.com.br/{}/discografia/index.js'.format(artist))

        try:
            response = response.json()

        except ValueError:
            raise ArtistNotFound

        albums_name = [disc['desc'] for disc in response['discography']['item']]

        data = {
            'artist': response['discography']['artist']['desc'],
            'albums': albums_name,
        }
        return data

    def getSongs(self, artist, album):
        songs = []
        artist = formating_string_name(artist)

        response = r.get(
            'http://www.vagalume.com.br/{}/discografia/index.js'.format(artist)
        )
        
        try:
            response = response.json()
        except ValueError:
            raise ArtistNotFound

        for discography in response['discography']['item']:
            if (discography['desc'] == album):
                songs = [
                    songs['desc'] for songs in discography['discs'][0]
                ]
                break

        if not songs:
            raise DiscographyNotFound
        # List songs from the album which the user chosen
        return songs
