from controller import API
from myexceptions import MusicNotFound, ArtistNotFound

artist = input("Artist name:")
music = input("Music name:")

api = API()

try:
	text = api.getLyrics(artist, music)
	print(text)
	
except MusicNotFound:
	print('Music not found!')

except ArtistNotFound:
	print('Artist not found!')
