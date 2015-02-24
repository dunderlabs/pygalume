from controller import API

artist = input("Artist name:")
music = input("Music name:")

api = API()
text = api.getLyrics(artist, music)

print(text)