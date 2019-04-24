# -*- coding: utf-8 -*-

#IMPORT MODULES
import os
import json
import requests
from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from SI507project_dbpopulate import *

#APPLICATION CONFIGURATION AND DATABASE SETUP -- consider separating into new file
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

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
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    venue_id = db.Column(db.Integer, db.ForeignKey("venue.id"))
    artists = db.relationship(
        "Artist",
        secondary=performances,
        back_populates="events")


    def __repr__(self):
        return "{} by {} at {} on {}".format(self.name, self.artist, self.venue_id, self.date)

class Artist(db.Model):
    __tablename__ = "artist"
    id = db.Column(db.Integer, primary_key=True)
    # artist_name = db.Column(db.String(64), unique=True)
    artist_name = db.Column(db.String(64))
    events = db.relationship(
        "Event",
        secondary=performances,
        back_populates="artists")


    def __repr__(self):
        return "Artist name: {} | ID: {}".format(self.artist_name, self.id)

class Genre(db.Model):
    __tablename__ = "genre"
    id = db.Column(db.Integer, primary_key=True)
    # genre_name = db.Column(db.String(64), unique=True)
    genre_name = db.Column(db.String(64))
    events = db.relationship("Event")

    def __repr__(self):
        return "Genre name: {} | ID: {}".format(self.genre_name, self.id)

class Venue(db.Model):
    __tablename__ = "venue"
    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(64), unique=True)
    name = db.Column(db.String(64))
    address = db.Column(db.String(250))
    city = db.Column(db.String(64))
    country = db.Column(db.String(64))
    events = db.relationship("Event")

    def __repr__(self):
        return "Venue: {} | City: {} | Country: {}".format(self.name, self.city, self.country)

class Song(db.Model):
    __tablename__ = "song"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    album = db.Column(db.String(250))
    length = db.Column(db.Integer) #check type
    artist_id = db.Column(db.Integer, db.ForeignKey("artist.id"))
    artists = db.relationship("Artist")

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
# venues_list = []
# genres_list = []
# artists_list = []
e = raw_events_data["_embedded"]["events"]

# for i in e:
#     print(type(i["_embedded"]))

#FlASK ROUTES - SAVE LISTS OF INSTANCES INTO THE DATABASE
@app.route('/') ##Home Page - links to other routes and instructions on how to use them
def index():
    for event_item in e:
        populate_artist = create_artist(artist_name=event_item["_embedded"]["attractions"][0]["name"])
        populate_venues = create_venue(event_item)
        populate_events = create_event(event_item, event_item["_embedded"]["attractions"][0]["name"], event_item["classifications"][0]["genre"]["name"], populate_artist)
        # print(event_item["classifications"][0]["genre"]["name"])
        populate_genre = create_genre(genre_name=event_item["classifications"][0]["genre"]["name"])
    return render_template("index.html")

@app.route('/events-per-location')
def filter_by_location():
    all_cities = []
    venues = Venue.query.all()
    for item in venues:
        all_cities.append(item.city)
    return render_template("location.html", all_cities=all_cities)

@app.route('/events-per-location/result', methods=['GET'])
def get_location_result():
    filtered_events = []
    if request.method == "GET":
        # print(request.args)
        for k in request.args:
            city = request.args.get(k,"None")
            # print(city)
            venues = Venue.query.filter_by(city=city)
            for item in venues:
                # print(item)
                events = Event.query.filter_by(venue_id=item.id)
                for ev in events:
                    filtered_events.append((ev.name, ev.date, item.name, item.city))
    return render_template("location_results.html", city=city, filtered_events=filtered_events)

@app.route('/events-per-genre')
def filter_by_genre():
    all_genre = []
    genre = Genre.query.all()
    for item in genre:
        all_genre.append(item.genre_name)
    return render_template("genre.html", all_genre=all_genre)

@app.route('/events-per-genre/result', methods=['GET'])
def get_genre_result():
    filtered_events = []
    if request.method == "GET":
        # print(request.args)
        for k in request.args:
            selected_genre = request.args.get(k,"None")
            # print(selected_genre)
            genre = Genre.query.filter_by(genre_name=selected_genre)
            for item in genre:
                # print(item)
                events = Event.query.filter_by(genre_id=item.id)
                for ev in events:
                    venues = Venue.query.filter_by(id=ev.venue_id)
                    for venue in venues:
                        filtered_events.append((ev.name, ev.date, venue.name, venue.city, venue.country))
    return render_template("genre_results.html", selected_genre=selected_genre, filtered_events=filtered_events)


@app.route('/events-per-artist')
def filter_by_artist():
    all_artists = []
    artists = Artist.query.all()
    for item in artists:
        all_artists.append(item.artist_name)
    return render_template("artists.html", all_artists=all_artists)

@app.route('/events-per-artist/result', methods=['GET'])
def get_artist_result():
    filtered_events = []
    if request.method == "GET":
        # print(request.args)
        for k in request.args:
            selected_artist = request.args.get(k,"None")
            # print(selected_artist)
            raw_songs_data = get_itunes_songs(selected_artist)
            s = raw_songs_data["results"]
            song_recs = []
            artists = Artist.query.filter_by(artist_name=selected_artist)
            for item in artists:
                # print(item.id)
                # associations = performances.query.filter_by(artist_id=item.id)
                events = Event.query.filter(Event.artists.any(id=item.id)).all()
                for ev in events:
                    venues = Venue.query.filter_by(id=ev.venue_id)
                    for venue in venues:
                        filtered_events.append((ev.name, ev.date, venue.name, venue.city, venue.country))

                for song_item in s:
                    populate_song = create_song(song_item, selected_artist)
                    songs = Song.query.filter_by(artist_id=item.id)
                    for song in songs[:10]:
                        song_recs.append((song.title))
    return render_template("artist_results.html", selected_artist=selected_artist, filtered_events=filtered_events, song_recs=song_recs)


#CREATE DATABASE AND RUN FLASK APP
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
