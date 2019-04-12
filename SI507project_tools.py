# -*- coding: utf-8 -*-

#IMPORT MODULES
import os
import json
import requests
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#DEFINE CLASSES - set relationships and instance variables
class Event(): #test with base class first, then define them as SQLAlchemy
    pass

class Artist():
    pass

class Genre():
    pass

class Venue():
    pass

class Song():
    pass


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


#GET DATA FROM APIs
raw_events_data = get_ticketmaster_music_events()
events_list = []

for data in raw_events_data["_embedded"]["events"]: #create instances for my classes and append them to list? or commit them directly to database?
    print(data)


#SETUP DATABASE -- consider separating into new file

#PROCESS DATA TO SAVE IT ON DATABASE
