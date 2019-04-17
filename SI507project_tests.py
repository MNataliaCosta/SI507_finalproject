import unittest
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

class Tables(unittest.TestCase):
    def test_events_instances(self):
        self.assertTrue(len(events_list)>0, "Testing instances of Event tables were created and saved to events_list")
    def test_venues_instances(self):
        self.assertTrue(len(venues_list)>0, "Testing instances of Venue tables were created and saved to venues_list")
    def test_genres_instances(self):
        self.assertTrue(len(genres_list)>0, "Testing instances of Genre tables were created and saved to genres_list")
    def test_artists_instances(self):
        self.assertTrue(len(artists_list)>0, "Testing instances of Artist tables were created and saved to artists_list")
    def test_songs_instances(self):
        self.assertTrue(len(songs_list)>0, "Testing instances of Song tables were created and saved to songs_list")

if __name__ == "__main__":
    unittest.main(verbosity=2)
