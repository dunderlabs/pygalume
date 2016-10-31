import argparse
import os
from .controller.factory import Factory
from .myexceptions import MusicNotFound, ArtistNotFound, DiscographyNotFound


factory = Factory()


def main():
    parser = argparse.ArgumentParser(
        prog='Pygalume',
        description="""A simple python command line utility using the Vagalume
                    API to search and show songs lyrics.""",
        usage="""
        Pygalume - Lyrics Finder

          Usage: pygalume.py [-a/--artist <artist-name>]
                             [-m/--music <music-name>]
                             [--al/--album <album-name>]
                             [-d/--discography]
                             [--lc/--list-cache]
                             [--cc/--clear-cache]
                             [-p/--pretty]
  \n              Get basic options and Help, use: -h\--help

          Examples:
            - Get Lyrics:
                 pygalume.py -a "Pearl Jam" -m Black

            - Get Lyrics (Versions side by side):
                 pygalume.py -a "Pearl Jam" -m Black -p

            - Get Discography:
                 pygalume.py -a "Pearl Jam" -d

            - Get Songs name from an album:
                 pygalume.py -a "Pearl Jam" --al "Ten"
              """
    )

    parser.add_argument(
        "-a",
        "--artist",
        dest="artist",
        type=str,
        help="Set artist name",
    )

    parser.add_argument(
        "-m",
        "--music",
        dest="music",
        type=str,
        help="Set music name",
    )

    parser.add_argument(
        "-p",
        "--pretty",
        action="store_true",
        help="Display song versions side by side",
    )

    parser.add_argument(
        "--al",
        "--album",
        dest="album",
        type=str,
        help="Set album name",
    )

    parser.add_argument(
        "-d",
        action="store_true",
        dest="discography",
        help="List all albums",
    )

    parser.add_argument(
        "--lc",
        action="store_true",
        dest="listCache",
        help="List all songs in cache",
    )

    parser.add_argument(
        "--cc",
        action="store_true",
        dest="cache",
        help="Clear the database cache",
    )

    options = parser.parse_args()

    artist = options.artist
    music = options.music
    album = options.album
    discography = options.discography
    listCache = options.listCache
    cache = options.cache
    pretty = options.pretty

    if cache:
        clearCache()
        return

    if listCache:
        getCachedMusics()
        return

    if artist and music:
        getLyrics(artist, music, pretty)
        return

    if artist and discography:
        getDiscography(artist)

    if artist and album:
        getSongs(artist, album)

    else:
        printHelpMessage()
        return


def printHelpMessage():
    print("""
Options:
  -h, --help                show this help message and exit

  -a, --artist <keyword>    set artist name
  -m, --music <keyword>     set music name
  --al, --album <keyword>   set album name
  -d, --discography         search for artist name

  --lc, --list-cache        list all songs in cache
  --cc, --clear-cache       clear cache from database

  -p, --pretty              display song versions side by side
            """)


def clearCache():
    os.remove('banco.db')
    print("Cache cleaned!")


def getCachedMusics():
    songs = factory.getCachedSongs()

    print('\n\n  Artist  -  Song')
    print('-------------------')
    for song in songs:
        print(song)
    print('\n\n')


def getLyrics(artist, music, pretty):
    try:
        data = factory.getLyrics(artist, music)

        if pretty and data.translate:
            print_pretty_lyrics(data)
        else:
            print_lyrics(data)

    except MusicNotFound:
        print('Music not found!')

    except ArtistNotFound:
        print('Artist not found!')


def getDiscography(artist):
    try:
        data = factory.getDiscography(artist)
        for disc in data['albums']:
            print(disc)

    except ArtistNotFound:
        print('Artist not found!')


def getSongs(artist, album):
    try:
        data = factory.getSongs(artist, album)
        for music in data:
            print(music)
    except DiscographyNotFound:
        print('Discography not found!')


def print_lyrics(data):
    print('\n-------------------------\n')
    print('Artist: {}'.format(data.artist))
    print('Song: {}'.format(data.music))
    print('URL: {}'.format(data.music_url))
    print('\n-------------------------\n')
    print(data.text)
    print('\n-------------------------\n')

    if data.translate:
        print(data.translate)
        print('\n-------------------------\n')


def print_pretty_lyrics(data):
    original_song = [x.strip() for x in data.text.split('\n')]
    translated_song = [x.strip() for x in data.translate.split('\n')]

    original_title = '[{0}]'.format(data.music)
    translated_title = translated_song.pop(0)

    while(translated_song and translated_song[0].strip() == ''):
        translated_song.pop(0)

    max_length = max([len(x) for x in original_song])

    text = prettify_title(data, original_title, translated_title, max_length)
    for i in range(len(original_song)):
        text += prettify_line(original_song[i], translated_song[i], max_length)

    text += '\n-------------------------\n'
    print(text)


def prettify_title(data, original, translated, max_length):
    text = '\n-------------------------\n\n'
    text += 'Artist: {}'.format(data.artist)
    text += '\n'
    text += 'URL: {}'.format(data.music_url)
    text += '\n\n-------------------------\n\n'
    text += prettify_line(original, translated, max_length)
    text += prettify_line('', '', max_length)
    return text


def prettify_line(original, translated, max_length):
    text = original + ' ' * (max_length - len(original))
    text += '{0}|{0}'.format(' ' * 10)
    text += translated
    text += '\n'
    return text


if __name__ == "__main__":
    main()
