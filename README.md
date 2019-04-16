# Ticketmaster Music Events - Flask Application

Natalia Costa

[Link to this repository](https://github.com/MNataliaCosta/SI507_finalproject)

---

## Project Description
This project aggregates music events data from Ticketmaster and song data from iTunes. It allows users to:
1. see how many events there currently are in a venue, city, or US;
2. see up to 10 events filtered by price, genre, or artist;
3. see up to 10 iTunes song suggestions based on the artist of selected event

## How to run
1. First, install all requirements with `pip install -r requirements.txt`
2. Second, run `python programname.py runserver`

## How to use
1. Open your browser and access http://localhost:5000
2. Interact with the application using the different routes available (see *Routes in this application* for more details )
3. (Optional): Markdown syntax to include an screenshot/image: ![alt text](image.jpg)

## Routes in this application
- `/` -> this is the home page and contains links to navigate to other routes
- `/events-per-location` -> shows the total number of Ticketmaster events currently available in the U.S; the user will also have the opportunity to see the number of events filtered by city or venue
- `/top-10-events` -> shows a list of up to 10 event recommendations, which will be provided based on the user input on genre or artist
- `/top-10-songs` -> shows a list of up to 10 iTunes songs of the artist of the selected event

## How to run tests - WORK IN PROGRESS
1. First... (e.g. access a certain directory if necessary)
2. Second (e.g. any other setup necessary)
3. etc (e.g. run the specific test file)
NOTE: Need not have 3 steps, but should have as many as are appropriate!

## In this repository: - WORK IN PROGRESS
- Directory Name
  - File in directory
  - File in directory
- File name
- File name

---
## Code Requirements for Grading - WORK IN PROGRESS
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [ ] Project is submitted as a Github repository
- [ ] Project includes a working Flask application that runs locally on a computer
- [ ] Project includes at least 1 test suite file with reasonable tests in it.
- [ ] Includes a `requirements.txt` file containing all required modules to run program
- [ ] Includes a clear and readable README.md that follows this template
- [ ] Includes a sample .sqlite/.db file
- [ ] Includes a diagram of your database schema
- [ ] Includes EVERY file needed in order to run the project
- [ ] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [ ] Includes at least 3 different routes
- [ ] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [ ] Interactions with a database that has at least 2 tables
- [ ] At least 1 relationship between 2 tables in database
- [ ] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [ ] Use of a new module
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [ ] A many-to-many relationship in your database structure
- [ ] At least one form in your Flask application
- [ ] Templating in your Flask application
- [ ] Inclusion of JavaScript files in the application
- [ ] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [ ] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [ ] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [ ] Caching of data you continually retrieve from the internet in some way

### Submission
- [ ] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [ ] I included a summary of my project and how I thought it went **in my Canvas submission**!
