# fullthrottle
# Search words from dataset with some specified constraints
# fullthrottle is the name of the project
# page3.html is the simple frontend html page based on jinja2 template language, jquery and css and javascript.

API Endpoints. GET http://localhost:8000 This endpoint renders a search box in the browser.

GET http://localhost:8000/search/?term=prac

the service might receive this sequence of requests, like:

GET http://localhost:8000/search/?term=prac

GET http://localhost:8000/search/?term=pract

GET http://localhost:8000/search/?term=practi and based on this search behavior, suggestions for searching words will show up in the browser.

GET http://localhost:800/searchResults/?term=prac

This endpoint finally returns a response which is of JSON array containing 25 results, ranked by criteria. 
wordsearch app has the main code. Dataset file is added to the project instead of using external database for content.
wordsearch/models.py has the code logic.
If no letters are found Django messages.info is used to display info on the same screen.
All the constraints mentioned in the test are satisfied.

