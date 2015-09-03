import optparse
import os
from controller import Factory
from myexceptions import MusicNotFound, ArtistNotFound


factory = Factory()


def main():
    parser = optparse.OptionParser(add_help_option=False)

    parser.add_option("-a", "--artist", dest="artist", type="string",
                                        help="Set artist name",)

    parser.add_option("-m", "--music", dest="music", type="string",
                                        help="Set music name",)

    parser.add_option("--al", "--album", dest="album", type="string",
                                        help="Set album name",)

    parser.add_option("-d", action="store_true", dest="discography",
                  help="List all albums")

    parser.add_option("--lc", action="store_true", dest="listCache",
                  help="List all music in cache")

    parser.add_option("--cc", action="store_true", dest="cache",
                  help="Clear the database cache")

    parser.add_option("--update",
                  action="store_true", dest="update",
                  help="upgrade to latest version")

    parser.add_option("-h", "--help",
                      action="store_true", dest="help", help="-h")
    
    (options, args) = parser.parse_args()

    argsParameters = {}
    artist = options.artist
    music = options.music
    album = options.album
    discography = options.discography
    listCache = options.listCache
    cache = options.cache
    help = options.help
    update = options.update
    
    if help:
       printHelpMessage()
       return

    if update:
        print("This is not working yet!")
        return
    
    if cache:
        clearCache()
        return

    if listCache:
        print("This is not working yet!")
        return

    if artist and music:
        getLyrics(artist, music)
        return

    if artist and discography:
        getDiscography(artist)

    if artist and album:
        getSongs(artist, album)

    else:
        basicInfo()
        return


def printHelpMessage():
     print("""
Options:
  -h, --help                show this help message and exit

  -a, --artist <keyword>    set artist name
  -m, --music <keyword>     set music name
  --al, --album <keyword>   set album name
  -d, --discography         search for artist name
  
  --lc, --list-cache        list all music in cache
  --cc, --clear-cache       clear cache from database

  --update                  upgrade to latest version
            """)


def clearCache():
    os.remove('banco.db')
    print("Cache cleaned!")


def basicInfo():
     print("""
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
              """)


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
    data = factory.getSongs(artist, album)
    for music in data:
        print(music)


if __name__ == "__main__":
    main()