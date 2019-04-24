import unittest
import sqlite3
from SI507project_tools import *

class Caching(unittest.TestCase):
    def test_cache_diction_existence(self):
        self.assertIsInstance(CACHE_DICTION, dict,"Testing that cache_diction is a dictionary")
    def test_cache_not_empty(self):
        testfile = open("SI507finalproject_cached_data.json","r")
        testfilestr = testfile.read()
        testfile.close()
        self.assertTrue(len(testfilestr)>0, "Testing that the cache file isn't empty")
    def test_cache_has_Ticketmater(self):
        testfile = open("SI507finalproject_cached_data.json","r")
        testfilestr = testfile.read()
        testfile.close()
        self.assertTrue("https://app.ticketmaster.com/discovery/v2/eventsclassificationName-music" in testfilestr, "Testing that Ticketmaster API was called and the music events result is in the cache file")
    def test_cache_has_iTunes(self):
        testfile = open("SI507finalproject_cached_data.json","r")
        testfilestr = testfile.read()
        testfile.close()
        self.assertTrue("https://itunes.apple.com/search" in testfilestr, "Testing that iTunes API was called and result is in the cache file")

class DBTests(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect("music_events.db")
        self.cur = self.conn.cursor()

    def test_for_artist_table(self):
        self.cur.execute("select artist_name from artist where artist_name = 'P!NK'")
        data = self.cur.fetchone()
        self.assertEqual(data,('P!NK',), "Testing data that results from selecting P!NK as an artist")

    def test_for_event_table(self):
        self.cur.execute("select name, date from event where name = 'Eagles'")
        data = self.cur.fetchone()
        self.assertEqual(data,('Eagles', '2019-09-28'), "Testing data that results from selecting Eagles as an event")

    def test_for_genre_table(self):
        self.cur.execute("select genre_name from genre where genre_name = 'Rock'")
        data = self.cur.fetchone()
        self.assertEqual(data,('Rock',), "Testing data that results from selecting Rock as a genre")

    def test_for_song_table(self):
        self.cur.execute("select title, album from song where title = 'Live and Let Die'")
        data = self.cur.fetchone()
        self.assertEqual(data,('Live and Let Die', 'Wings Greatest'), "Testing data that results from selecting Live and Let Die as a song")

    def test_for_venue_table(self):
        self.cur.execute("select city from venue where name = 'T-Mobile Arena'")
        data = self.cur.fetchone()
        self.assertEqual(data,('Las Vegas',), "Testing data that results from selecting T-Mobile Arena as a song")

# class Tables(unittest.TestCase):
#     def test_events_instances(self):
#         self.assertTrue(len(events_list)>0, "Testing instances of Event tables were created and saved to events_list")
#     def test_venues_instances(self):
#         self.assertTrue(len(venues_list)>0, "Testing instances of Venue tables were created and saved to venues_list")
#     def test_genres_instances(self):
#         self.assertTrue(len(genres_list)>0, "Testing instances of Genre tables were created and saved to genres_list")
#     def test_artists_instances(self):
#         self.assertTrue(len(artists_list)>0, "Testing instances of Artist tables were created and saved to artists_list")
#     def test_songs_instances(self):
#         self.assertTrue(len(songs_list)>0, "Testing instances of Song tables were created and saved to songs_list")

if __name__ == "__main__":
    unittest.main(verbosity=2)
