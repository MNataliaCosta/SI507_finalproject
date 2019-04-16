# -*- coding: utf-8 -*-

#IMPORT MODULES
import os
import json
import requests
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#APPLICATION CONFIGURATION AND DATABASE SETUP -- consider separating into new file
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'ngrjfdnjngdsfngdipfng'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./music_events.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
session = db.session


#DEFINE CLASSES - set relationships and instance variables
performances = db.Table('performance',db.Column('event_id',db.Integer, db.ForeignKey('event.id'), primary_key=True),db.Column('artist_id',db.Integer, db.ForeignKey('artist.id'), primary_key=True))


class Event(db.Model):
    # def __init__(self): -- test
        # self.artist = d["_embedded"]["attractions"][0]["name"]
        # self.venue = d["_embedded"]["venues"][0]["name"]
    __tablename__ = "event"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    date = db.Column(db.String(64))
    artists = db.relationship("Artist", secondary=performances, backref=db.backref("event"))
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    venue_id = db.Column(db.Integer, db.ForeignKey("venue.id"))


    def __repr__(self):
        return "{} by {} at {} on {}".format(self.name, self.artist_id, self.venue_id, self.date)

class Artist(db.Model):
    __tablename__ = "artist"
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(64), unique=True)


    def __repr__(self):
        return "Artist name: {} | ID: {}".format(self.artist_name, self.id)

class Genre(db.Model):
    __tablename__ = "genre"
    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(64), unique=True)
    events = db.relationship("Event")

    def __repr__(self):
        return "Genre name: {} | ID: {}".format(self.gente_name, self.id)

class Venue(db.Model):
    __tablename__ = "venue"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    address = db.Column(db.String(250))
    city = db.Column(db.String(64))
    country = db.Column(db.String(64))
    events = db.relationship("Event")

    def __repr__(self):
        return "Venue: {} | City: {} | State: {}".format(self.name, self.city, self.state)

class Song(db.Model):
    __tablename__ = "song"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    album = db.Column(db.String(250))
    length = db.Column(db.Integer) #check type
    artist_id = db.Column(db.Integer, db.ForeignKey("artist.id"))
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    artists = db.relationship("Artist")
    genres = db.relationship("Genre")


#DEFINE CACHING PATTERN
CACHE_FNAME = "SI507finalproject_cached_data.json"

try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION ={}

def params_unique_combination(baseurl, params_d, private_keys=["apikey"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)


#DEFINE API FUNCTIONS
##Ticketmaster music events_list
TICKETMASTER_KEY = "flOylULADXO43hT6xYjAcuIef4ZxTwhB"

def get_ticketmaster_music_events():
    ticketmaster_baseurl = "https://app.ticketmaster.com/discovery/v2/events"
    ticketmaster_d_params = {}
    ticketmaster_d_params["apikey"] = TICKETMASTER_KEY
    ticketmaster_d_params["classificationName"] = "music"
    unique_identifier = params_unique_combination(ticketmaster_baseurl, ticketmaster_d_params)

    if unique_identifier in CACHE_DICTION:
        return CACHE_DICTION[unique_identifier]
    else:
        ticketmaster_resp = requests.get(ticketmaster_baseurl, params = ticketmaster_d_params)
        ticketmaster_obj = json.loads(ticketmaster_resp.text)
        cache_file_obj = open(CACHE_FNAME, 'w')
        CACHE_DICTION[unique_identifier] = ticketmaster_obj
        cache_file_obj.write(json.dumps(CACHE_DICTION))
        cache_file_obj.close()
        return ticketmaster_obj

##iTunes songs
def get_itunes_songs(artist_result):
    iTunes_baseurl = "https://itunes.apple.com/search"
    iTunes_d_params = {}
    iTunes_d_params["term"] = artist_result #required param
    iTunes_d_params["media"] = "music" #optional param
    iTunes_d_params["entity"] = "song" #optional param
    # iTunes_d_params["limit"] = "20" #optional param, default = 50
    unique_identifier = params_unique_combination(iTunes_baseurl, iTunes_d_params)

    if unique_identifier in CACHE_DICTION:
        return CACHE_DICTION[unique_identifier]
    else:
        iTunes_resp = requests.get(iTunes_baseurl, params = iTunes_d_params)
        iTunes_obj = json.loads(iTunes_resp.text)
        cache_file_obj = open(CACHE_FNAME, 'w')
        CACHE_DICTION[unique_identifier] = iTunes_obj
        cache_file_obj.write(json.dumps(CACHE_DICTION))
        cache_file_obj.close()
        return iTunes_obj


#GET DATA FROM APIs
raw_events_data = get_ticketmaster_music_events()
# events_list = []

# raw_songs_data = get_itunes_songs(artist_result)
raw_songs_data = get_itunes_songs("Ariana Grande")
# songs_list = []


#PROCESS DATA TO SAVE IT ON DATABASE
for e in raw_events_data["_embedded"]["events"]: #create instances for my classes and append them to list? or commit them directly to database?
    print(e["_embedded"]["venues"][0]["country"]["name"])
    # new_event = Event(name=e["name"], date=e["dates"]["start"]["localDate"] , artists= , genre_id=, venue_id=, )
    # artist = Artist()
    # new_genre = Genre(genre_name=events_data["classifications"][0]["genre"]["name"])
    # new_venue = Venue(name=e["_embedded"]["venues"][0]["name"] , address=e["_embedded"]["venues"][0]["address"]["line1"] , city=e["_embedded"]["venues"][0]["city"]["name"] , country=e["_embedded"]["venues"][0]["country"]["name"])

    # session.add(new_genre)
    # session.commit()


# for i in events_list:
#     print(i)

# def get_or_create_artist(artist_name):
#     artist = Artist.query.filter_by(name=artist_name).first()
#     if artist:
#         return artist
#     else:
#         artist = Artist(name=artist_name)
#         session.add(artist)
#         session.commit()
#         return artist


for s in raw_songs_data["results"]: #create instances for my classes and append them to list? or commit them directly to database?
    print(s["trackTimeMillis"])
    # new_song = Song(title=s["trackName"], album=s["collectionName"], length=s["trackTimeMillis"], artist_id=artist.id, genre_id=genre.id)


if __name__ == '__main__':
    db.create_all()
    # app.run()
