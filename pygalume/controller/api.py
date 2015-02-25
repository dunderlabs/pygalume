import requests as r
from settings import API_URL
from .utils import formating_string_name
from .myexceptions import MusicNotFound, ArtistNotFound


SONG_NOT_FOUND = 'song_notfound'
NOT_FOUND = 'notfound'


class API():

	def getLyrics(self, artist, music):
		artist = formating_string_name(artist)
		music = formating_string_name(music)

		response = r.get(API_URL+'art={0}&mus={1}'.format(artist, music))
		
		if response.json()['type'] == SONG_NOT_FOUND:
			raise MusicNotFound

		elif response.json()['type'] == NOT_FOUND:
			raise ArtistNotFound

		else:
			return response.json()['mus'][0]['text']


