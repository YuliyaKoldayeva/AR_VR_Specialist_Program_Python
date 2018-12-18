"""
8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
"""

 # 8-7
print("\t Solution for 8-7")
def make_album(artist_name, album_title, number_of_tracks):
   album_dic_8_7 = {"artist": artist_name, "album": album_title, "tracks": number_of_tracks}
   return album_dic_8_7


for album in range(3):
    artist_name = input("Type the name of the artist: ").title()
    album_title = input("Type the title of the album: ").title()
    add_number_of_tracks = input("Would you like to add the number of tracks? (Y/N) ").upper()
    if add_number_of_tracks == "Y":
        number_of_tracks = str(input("Type the number of tracks: "))
    else:
        number_of_tracks = "Number of tracks is unknown"

    print(make_album(artist_name, album_title, number_of_tracks))

print("*******************************")
 # 8-8
print("\t Solution for 8-8")
def make_album(artist_name, album_title):
   album_dic_8_8 = {"artist": artist_name, "album": album_title}
   return album_dic_8_8


while True:
    print('Type "stop" to finish.')
    artist_name = input("Type the name of the artist: ").title()
    if artist_name=="Stop":
        break
    album_title = input("Type the title of the album: ").title()
    if album_title =="Stop":
        break
    print(make_album(artist_name, album_title))