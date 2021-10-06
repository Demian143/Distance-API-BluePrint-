import requests
import time
import os
from bs4 import BeautifulSoup
from geopy import distance


API_KEY = os.environ['API_KEY']  # Set your own api key in the env file


class Search:
    MKAD = (37.842762, 55.774558)  # Static point to be calculated (longlat)

    def search_soup(self, address):
        """ Searchs for a place by coordenates or address,
        takes the tag inside the tag.

        Attention! The given document has coordenates in long/lat format,
        so it searchs in this format. To change the format,
        simply change the <'sco'>variable in the link to <'latlong'>. """

        url = "https://geocode-maps.yandex.ru/1.x/?apikey={}&geocode={}&results=1&sco=longlat&lang=en-US".format(
            API_KEY, address)

        # parses the html
        driver = requests.get(url)
        page = BeautifulSoup(driver.content, 'html.parser')

        dictionary = {}

        # take infomation inside a tag
        for tag in ['Point', 'Address']:
            try:
                tag_text = page.select_one(tag).text
                dictionary.update({tag: tag_text})

            except AttributeError:
                dictionary.update({tag: 'Not found'})

        return dictionary

    def calc_distance(self, address):
        """ Calc the distance from a local in km,default local will be mkad (But you can change it),
            if the place is inside the mkad it doesn't make the calc """

        words = ['mkad', 'MKAD']
        soup = self.search_soup(address)

        try:
            for word in words:
                if word in soup['Address']:
                    return "Your address is inside MKAD, there's no need to calculate the distance."

            else:
                point = soup['Point']
                distance_km = distance.distance(MKAD, point)
                return distance_km

        except ValueError:
            return 'Sorry, something went wrong'


# MKAD = (37.842762, 55.774558)
# test = (37.618423, 55.751244)

# search = Search()
# x = search.search_soup(MKAD)
# print(x)

# y = search.calc_distance(MKAD)
# print(y)
