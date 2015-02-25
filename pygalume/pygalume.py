from controller import API
from myexceptions import MusicNotFound, ArtistNotFound

artist = input("Artist name:")
music = input("Music name:")

api = API()

try:
	data = api.getLyrics(artist, music)
	print(data['text'])
	print('\n ------------------------- \n')
	print(data['translate'])
	
except MusicNotFound:
	print('Music not found!')

except ArtistNotFound:
	print('Artist not found!')
