from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from geopy import distance

options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

API_KEY = "dba4558d-b961-4e34-bd1f-6b8837626a8d"
MKAD = (55.751244, 37.618423)  # static point to be calculated
test = (37.842762, 55.774558)  # any other place to take as parameter

# searchs for a place by cordenates or verbose name
# I need to make sure if the lowercase is the right coordenate


def search_geocode(geocode):
    url = "https://geocode-maps.yandex.ru/1.x/?apikey={}&geocode={}&lang=en-US".format(
        API_KEY, geocode)
    driver.get(url)
    ll = driver.find_element_by_tag_name('Point')
    return ll.text


# calc distance in km, de default local1 will be mkad
def calc_distance(local2):
    result = distance.distance(MKAD, local2)
    return result
