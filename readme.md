### What does it do?

This is a flask blueprint that recievies a http request of an address and returns
the distance from MKAD. 
If the place is inside of MKAD, it doesn't make the calculus, instead it returns:
"Your address is inside MKAD, there's no need to calculate the distance."

### Supported formats:

The distance_api supports strings like "Moskow" and coordinates like "37.842762, 55.774558".
But there's one thing to remember, the coordinates passed to the application are in longlat
format. 
To use latlong go to flask_app/blueprints/distance_api/scrapper.py and read the instructions in the code. 

### How to run the application:

First of all, you'll need to make sure you have your own api key, 
go to https://yandex.ru/dev/maps/geocoder/doc/desc/concepts/about.html and register a geocoder api key.

1) run shell: source example.env
2) run shell: flask run
3) web browser: http://127.0.0.1:5000/api/v1/distance/<address>
