from SI507project_tools import *

e = raw_events_data["_embedded"]["events"]
s = raw_songs_data["results"]


def get_or_create_artist(dict):
    artist = Artist.query.filter_by().first()
    if artist:
        return artist
    else:
        artist = Artist(artist_name=dict["_embedded"]["attractions"][0]["name"], event_id=event.id) ## need to include artist?
        session.add(artist)
        session.commit()
        return artist

def get_or_create_venue(dict):
    venue = Venue.query.filter_by(name=dict["_embedded"]["venues"][0]["name"]).first()
    if venue:
        return venue
    else:
        venue = Venue(name=dict["_embedded"]["venues"][0]["name"] , address=dict["_embedded"]["venues"][0]["address"]["line1"] , city=dict["_embedded"]["venues"][0]["city"]["name"], country=dict["_embedded"]["venues"][0]["country"]["name"])
        session.add(venue)
        session.commit()
        return venue

def get_or_create_genre(dict):
    genre = Genre.query.filter_by(genre_name=dict["classifications"][0]["genre"]["name"]).first()
    if genre:
        return genre
    else:
        genre = Genre(genre_name=dict["classifications"][0]["genre"]["name"])
        session.add(genre)
        session.commit()
        return genre

def get_or_create_song(dict): ##how to get the event chosen as input?
    song = Song.query.filter_by(title=dict["trackName"]).first()
    if song:
        return song
    else:
        check_artist = get_or_create_artist(dict)
        song = Song(title=dict["trackName"], album=dict["collectionName"], length=dict["trackTimeMillis"], artist_id=artist.id, genre_id=genre.id)
        session.add(song)
        session.commit()
        return song

def get_or_create_event(dict): #what are the params?
    event = Event.query.filter_by(name=dict["name"]).first()
    if event:
        return event
    else:
        check_genre = get_or_create_genre(dict)
        check_venue = get_or_create_venue(dict)
        event = Event(name=dict["name"], date=dict["dates"]["start"]["localDate"], genre_id=check_genre.id, venue_id=check_venue.id)
        session.add(event)
        session.commit()
        return event

for event_item in e:
    get_or_create_artist(event_item)
    get_or_create_venue(event_item)
    get_or_create_genre(event_item)
    get_or_create_event(event_item)

for song_item in s:
    get_or_create_song(song_item)

#PROCESS DATA API DATA INTO LISTS OF THE DIFFERENT TABLE INSTANCES
# for e in raw_events_data["_embedded"]["events"]:
    # print(e["_embedded"]["venues"][0]["country"]["name"])
    # new_event = Event(name=e["name"], date=e["dates"]["start"]["localDate"] , artists= , genre_id=, venue_id=, )
    # artist = Artist()
    # if e["classifications"][0]["genre"]["name"] not in genres_list:
    #      new_genre = Genre(genre_name=e)
    #      genres_list.append(new_genre)
    #      session.add(new_genre)
    #      session.commit()
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
