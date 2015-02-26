from controller import API
from myexceptions import MusicNotFound, ArtistNotFound


api = API()

op = int(input(
	'''
	1 - Get Lyric
	2 - Get Discography
	Option: 
	'''
	))

if op == 1:
	artist = input("Artist name:")
	music = input("Music name:")

	try:
		data = api.getLyrics(artist, music)
		print(data['text'])
		print('\n ------------------------- \n')
		print(data['translate'])
		
	except MusicNotFound:
		print('Music not found!')

	except ArtistNotFound:
		print('Artist not found!')

elif op == 2:
	artist = input("Artist name:")
	
	try:
		data = api.getDiscography(artist)
		for disc in data['albums']:
			print(disc)

	except ArtistNotFound:
		print('Artist not found!')
