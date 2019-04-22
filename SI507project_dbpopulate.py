from SI507project_tools import *

e = raw_events_data["_embedded"]["events"]
s = raw_songs_data["results"]

def get_or_create_event(e): #what are the params?
    pass

def get_or_create_artist(e):
    pass

def get_or_create_venue(e):
    venue = Venue.query.filter_by(name=e["_embedded"]["venues"][0]["name"]).first()
    if venue:
        return venue
    else:
        venue = Venue(name=e["_embedded"]["venues"][0]["name"] , address=e["_embedded"]["venues"][0]["address"]["line1"] , city=e["_embedded"]["venues"][0]["city"]["name"], country=e["_embedded"]["venues"][0]["country"]["name"])
        session.add(venue)
        session.commit()
        return venue

def get_or_create_genre(e):
    genre = Genre.query.filter_by(genre_name=e["classifications"][0]["genre"]["name"]).first()
    if genre:
        return genre
    else:
        genre = Genre(genre_name=e["classifications"][0]["genre"]["name"])
        session.add(genre)
        session.commit()
        return genre

def get_or_create_song(s):
    pass




#PROCESS DATA API DATA INTO LISTS OF THE DIFFERENT TABLE INSTANCES
for e in raw_events_data["_embedded"]["events"]:
    # print(e["_embedded"]["venues"][0]["country"]["name"])
    # new_event = Event(name=e["name"], date=e["dates"]["start"]["localDate"] , artists= , genre_id=, venue_id=, )
    # artist = Artist()
    if e["classifications"][0]["genre"]["name"] not in genres_list:
         new_genre = Genre(genre_name=e)
         genres_list.append(new_genre)
         session.add(new_genre)
         session.commit()
    # new_venue = Venue(name=e["_embedded"]["venues"][0]["name"] , address=e["_embedded"]["venues"][0]["address"]["line1"] , city=e["_embedded"]["venues"][0]["city"]["name"] , country=e["_embedded"]["venues"][0]["country"]["name"])
    #

# def get_or_create_artist(artist_name):
#     artist = Artist.query.filter_by(name=artist_name).first()
#     if artist:
#         return artist
#     else:
#         artist = Artist(name=artist_name)
#         session.add(artist)
#         session.commit()
#         return artist
