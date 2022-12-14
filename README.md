# LoftyBackendCodeTest

\\\\\\\///////

Lofty Engineering Practical

Python/Backend

///////\\\\\\\

This backend attempts to solve the following client requests:
- Key Handling
	- Endpoint allows key creation as strings with a default int value
	- Endpoint to increment any given keys default value
	- Endpoint to list all keys and their values
- Dog Picture Handling
	- Populate database with 24 images of dogs via the api https://dog.ceo/dog-api/documentation/
	- Endpoint returns a normal dog image, and one manipulated/edited dog image (same image used for editing)

--------------------

# Setup for Development

Setup steps
- If folder downloaded directly
1) Extract 'LoftyCodeTest' folder somewhere (easiest is on /desktop)
2) Open 'LoftyCodeTest' folder, from chosen location, in IDE (Pycharm was used to develop)
- Else
1) Open IDE 
2) 'cd' into folder location preferred; do a 'git clone https://github.com/chadandex/LoftyBackendCodeTest.git' command
3) Make sure Docker is running; type and run the command: docker-compose up -d --build
4) type and run the command: docker-compose exec web python manage.py migrate 
   5) create a superuser
5) start docker with the command: docker-compose up
6) On Chrome or Firefox (Edge not tested), go to url http://localhost:8000/
7) If the page outputs text that says "There's nothing here..." then we're successful!

--------------------

API URLS
--------
**/api/doginfo/**

[POST]
- Saves 24 random dog pictures to database when called
- Returns a string message displaying what got saved

[GET] 
- Retrieves a single random picture from database. Attempts to manipulate that said image after retrieving.
- Returns 2 image urls to display on page. One for unedited picture. One for edited picture.


**/api/keyinfo/**

[POST] 
- Saves a key with a random default value, and user input 'name' value.
- Send a 'name' value in the request
- Return a JsonResponse with a message of the newly added key

[GET]
- Retrieves the full list of keys from database
- Returns a JsonResponse with a data dict containing a 'items' and 'count' value.


**/api/incrementkey/<int:value>/**

[GET] 
- Send a integer value where <int:value> is located when calling
- Increments a random key's default value with value sent
- Incrementing will multiprocess a single addition & a continuous 10 second addition
- Returns a JsonResponse with a data dict including a 'message' value