# Ticketmaster Music Events - Flask Application

Natalia Costa

[Link to this repository](https://github.com/MNataliaCosta/SI507_finalproject)

---

## Project Description
This project aggregates music events data from Ticketmaster and song data from iTunes. It allows users to:
1. search events by city;
2. search events by genre;
3. search events by artist and see a list of 10 recommended songs for the selected artist


## How to run
1. Using your command line interface (e.g. GitBash), access the directory where the project files are saves  
2. Install all requirements with `pip install -r requirements.txt`
3. Run `python SI507project_tools.py runserver`

## How to use
1. Open your browser and access http://localhost:5000
2. Interact with the application using the different routes available (see *Routes in this application* for more details )
3. (Optional): Markdown syntax to include an screenshot/image: ![alt text](image.jpg)

## Routes in this application
* `/` - home page; provide an overview of what the application does and how it works, including the links to navigate to the possible routes
* `/events-per-location` - using the dropdown form, the user can select which city currently available in the database to search for events and submit the search
* `/events-per-location/result` - displays a list of events based on the search by city
* `/events-per-genre` - using the dropdown form, the user can select which genre currently available in the database to search for events and submit the search
* `/events-per-genre/result` - displays a list of events based on the search by genre
* `/events-per-artist` - using the dropdown form, the user can select which artist currently available in the database to search for events and submit the search
* `/events-per-artist/result` - displays a list of events based on the search by artist as well as list of 10 recommended songs of the artist

## How to run tests
1. Make sure you have SQLite3 installed
2. Using your command line interface (e.g. GitBash), access the directory where the project files are saves
3. Run `python SI507project_tests.py`
4. There are currently 9 tests in the test suite; all of them should pass for the code to be properly working

## In this repository:
- SI507project_tools.py
- SI507project_dbpopulate.py
- SI507project_tests.py
- templates
  - index.html
  - location.html
  - location_results.html
  - genre.html
  - genre_results.html
  - artists.html
  - artist_results.html
- SI507finalproject_cached_data
- music_events.db
- README.md
- [507] Events Database Diagram.jpg
- requirements.txt

---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [x] Project is submitted as a Github repository
- [x] Project includes a working Flask application that runs locally on a computer
- [x] Project includes at least 1 test suite file with reasonable tests in it.
- [x] Includes a `requirements.txt` file containing all required modules to run program
- [x] Includes a clear and readable README.md that follows this template
- [x] Includes a sample .sqlite/.db file
- [x] Includes a diagram of your database schema
- [x] Includes EVERY file needed in order to run the project
- [x] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [x] Includes at least 3 different routes
- [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [x] Interactions with a database that has at least 2 tables
- [x] At least 1 relationship between 2 tables in database
- [x] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [ ] Use of a new module
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [x] A many-to-many relationship in your database structure
- [x] At least one form in your Flask application
- [x] Templating in your Flask application
- [ ] Inclusion of JavaScript files in the application
- [x] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [ ] Sourcing of data using web scraping
- [x] Sourcing of data using web REST API requests
- [ ] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [x] Caching of data you continually retrieve from the internet in some way

### Submission
- [x] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [x] I included a summary of my project and how I thought it went **in my Canvas submission**!
