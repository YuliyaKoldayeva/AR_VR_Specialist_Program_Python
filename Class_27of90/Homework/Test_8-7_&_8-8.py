"""
8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.

Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number
of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album.

8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
"""

# 8-7

def make_album(artist_name, album_title, number_of_tracks):
    album_description = (album_title.title(), number_of_tracks)
    album_dic = {artist_name.title(): album_description}
    return album_dic


for album in range(3):
    artist_name = input("Print a name of the artist: ")
    album_title = input("Print a title of the album: ")
    add_number_of_tracks = input("Would you like to add the number of tracks? (Y/N) ")
    if add_number_of_tracks.upper() == "Y":
        number_of_tracks = input("Type the number of tracks: ")
    else:
        number_of_tracks = "Number of tracks is unknown"

    print(make_album(artist_name, album_title, number_of_tracks))



# 8-8

def make_album(artist_name, album_title):

    album_dic = {artist_name.title(): album_title.title()}
    return album_dic

while True:
    print('Type "quit" to finish.')
    artist_name = input("Print a name of the artist: ")
    album_title = input("Print a title of the album: ")
    if artist_name=="quit" or album_title =="quit":
        break
    print(make_album(artist_name, album_title))