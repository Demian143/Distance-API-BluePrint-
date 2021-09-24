from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from geopy import distance
import time

options = Options()
options.add_argument('--headless')
options.add_argument('disable-infobars')
options.add_argument('disable-extentions')
options.add_argument('--no-sandbox')
options.add_argument('--disable-application-cache')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')


driver = webdriver.Firefox(options=options)

API_KEY = "dba4558d-b961-4e34-bd1f-6b8837626a8d"
MKAD = (55.751244, 37.618423)  # static point to be calculated

test = (37.842762, 55.774558)  # any other place to take as parameter


def generator_search(address):
    """ Searchs for a place by cordenates or address,
        takes a tag the information inside a the information inside of it,. """

    url = "https://geocode-maps.yandex.ru/1.x/?apikey={}&geocode={}&lang=en-US".format(
        API_KEY, address)
    driver.get(url)
    tags = ['Point', 'Address']
    dictionary = {}

    try:
        for tag in tags:
            tag_text = driver.find_element_by_tag_name(
                tag)  # search for the tag

            dictionary.update({tag: tag_text.text})

            time.sleep(1)

    except NoSuchElementException:
        dictionary.update({tag: 'Not Found'})

    finally:
        driver.close()
        return dictionary


x = generator_search(test)
print(x)


def find_tags(address):
    """ Takes the address and passes it to the <generator_search()>.
        After that, it takes the text to a dictionary with format:
        {tag: information} """

    tags = ['Point', 'Address']
    dictionary = {}
    try:
        for i in tags:
            x = generator_search(address)
            dictionary.update({i: x})
            time.sleep(2)

    except ValueError:
        return 'Sorry, looks like there is no results'
    return dictionary


def calc_distance(local2):
    """ Calc the distance in km, de default local1 will be mkad, 
        if the place is inside the mkad it doesent make the calc """

    words = ['mkad', 'MKAD']
    take_point = find_tags(local2)

    try:
        for word in words:
            if word in take_point['Address']:
                return f"Yor address is inside MKAD,there's no need to calculate the distance."
            else:
                return distance.distance(MKAD, take_point['Point'])
    except ValueError:
        return 'Sorry, looks like there is no results'


"""
a = find_tags('Moskow')
c = calc_distance(a)
print(next(c))
"""
