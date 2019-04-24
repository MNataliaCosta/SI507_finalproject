from SI507project_tools import *

def create_event(dict, name, genre, artist):
    event = Event.query.filter_by(name=name).first()
    if event:
        return event
    else:
        check_genre = create_genre(genre)
        check_venue = create_venue(dict)
        event = Event(name=dict["name"], date=dict["dates"]["start"]["localDate"], genre_id=check_genre.id, venue_id=check_venue.id)
        event.artists.append(artist)
        session.add(event)
        session.commit()
        return event

def create_artist(artist_name):
    artist = Artist.query.filter_by(artist_name=artist_name).first()
    if artist:
        return artist
    else:
        artist = Artist(artist_name=artist_name)
        session.add(artist)
        session.commit()
        return artist

def create_venue(dict):
    venue = Venue.query.filter_by(name=dict["_embedded"]["venues"][0]["name"]).first()
    if venue:
        return venue
    else:
        venue = Venue(name=dict["_embedded"]["venues"][0]["name"] , address=dict["_embedded"]["venues"][0]["address"]["line1"] , city=dict["_embedded"]["venues"][0]["city"]["name"], country=dict["_embedded"]["venues"][0]["country"]["name"])
        session.add(venue)
        session.commit()
        return venue

def create_genre(genre_name):
    genre = Genre.query.filter_by(genre_name=genre_name).first()
    if genre:
        return genre
    else:
        genre = Genre(genre_name=genre_name)
        session.add(genre)
        session.commit()
        return genre

def create_song(dict, artist_name): ##how to get the event chosen as input?
    song = Song.query.filter_by(title=dict["trackName"]).first()
    if song:
        return song
    else:
        check_artist = create_artist(artist_name)
        song = Song(title=dict["trackName"], album=dict["collectionName"], length=dict["trackTimeMillis"], artist_id=check_artist.id)
        session.add(song)
        session.commit()
        return song
