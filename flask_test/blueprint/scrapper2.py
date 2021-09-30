from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from geopy import distance
import os


API_KEY = os.environ['API_KEY']  # Set your own api key in the env file

test = (37.618423, 55.751244)  # Static point to be calculated (longlat)
MKAD = (37.842762, 55.774558)  # any other place to take as parameter (longlat)


class Search:

    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=options)

    def search_soup(self, address):
        """ Searchs for a place by coordenates or address,
        takes the tag inside the tag.

        Attention! The given document has coordenates in long/lat format,
        so it searchs in this format. To change the format,
        simply change the <'sco'>variable in the link to <'latlong'>. """

        url = "https://geocode-maps.yandex.ru/1.x/?apikey={}&geocode={}&results=1&sco=longlat&lang=en-US".format(
            API_KEY, address)
        # parses the html
        self.driver.get(url)
        page = BeautifulSoup(self.driver.page_source, 'html.parser')
        self.driver.quit()
        tags = ['Point', 'Address']
        dictionary = {}

        # take infomation inside a tag
        for tag in tags:
            try:
                find_tag = page.select_one(tag).text
                dictionary.update({tag: find_tag})

            except AttributeError:
                dictionary.update({tag: 'Not found'})

        return dictionary

    def calc_distance(self, address):
        """ Calc the distance in km, de default local1 will be mkad,
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


search = Search()
# x = search.search_soup(MKAD)
# print(x)

# y = search.calc_distance(MKAD)
# print(y)
