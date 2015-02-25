import requests as r
from settings import API_URL
from .utils import formating_string_name
from myexceptions import MusicNotFound, ArtistNotFound


SONG_NOT_FOUND = 'song_notfound'
NOT_FOUND = 'notfound'


class API():

	def getLyrics(self, artist, music):
		artist = formating_string_name(artist)
		music = formating_string_name(music)

		response = r.get(API_URL+'art={0}&mus={1}'.format(artist, music))

		response = response.json()
		
		if response['type'] == SONG_NOT_FOUND:
			raise MusicNotFound

		elif response['type'] == NOT_FOUND:
			raise ArtistNotFound

		else:
			# If the song is in portuguese, for example, there is no translation.
			try:
				translate = response['mus'][0]['translate']
				translate = translate[0]['text']
			except KeyError:
				translate = ''

			data = {
				'artist': response['art']['name'],
				'artist-url': response['art']['url'],
				'music': response['mus'][0]['name'],
				'music-url': response['mus'][0]['url'], 
				'text': response['mus'][0]['text'],
				'translate': translate,
			}
			return data
