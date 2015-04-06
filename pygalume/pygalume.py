from controller import Factory
from myexceptions import MusicNotFound, ArtistNotFound

factory = Factory()

op = int(input(
    '''
    1 - Get Lyric
    2 - Get Discography
    3 - Get Songs
    Option:
    '''
    ))

if op == 1:
    artist = input("Artist name: ")
    music = input("Music name: ")

    try:
        data = factory.getLyrics(artist, music)
        print(data.text)
        print('\n-------------------------\n')
        print(data.translate)

    except MusicNotFound:
        print('Music not found!')

    except ArtistNotFound:
        print('Artist not found!')

elif op == 2:

    artist = input("Artist name:")

    try:
        data = factory.getDiscography(artist)
        for disc in data['albums']:
            print(disc)

    except ArtistNotFound:
        print('Artist not found!')

elif op == 3:
    artist = input("Artist name: ")
    album = input("Album name: ")
    data = factory.getSongs(artist, album)
    print(data)
