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
  \n              Get basic options and Help, use: -h\--help

          Examples:
            - Get Lyrics:
                 pygalume.py -a "Pearl Jam" -m Black

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

    parser.add_argument(
        "--update",
        action="store_true",
        dest="update",
        help="upgrade to latest version",
    )

    options = parser.parse_args()

    artist = options.artist
    music = options.music
    album = options.album
    discography = options.discography
    listCache = options.listCache
    cache = options.cache
    update = options.update

    if update:
        print("This is not working yet!")
        return

    if cache:
        clearCache()
        return

    if listCache:
        getCachedMusics()
        return

    if artist and music:
        getLyrics(artist, music)
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

  --update                  upgrade to latest version
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


def getLyrics(artist, music):
    try:
        data = factory.getLyrics(artist, music)
        print(data.text)
        print('\n-------------------------\n')
        print(data.translate)

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


if __name__ == "__main__":
    main()
