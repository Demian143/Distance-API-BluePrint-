from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from geopy import distance

options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

API_KEY = "dba4558d-b961-4e34-bd1f-6b8837626a8d"
MKAD = (55.751244, 37.618423)  # static point to be calculated
test = (37.842762, 55.774558)  # any other place to take as parameter


def generator_search(tag,  geocode):
    """ Searchs for a place by cordenates or address,
        it takes a tag and prints out the information inside of it.
        Need te function <find_tags()> to make i work. """

    url = "https://geocode-maps.yandex.ru/1.x/?apikey={}&geocode={}&lang=en-US".format(
        API_KEY, geocode)
    driver.get(url)

    try:
        # search for the tag
        locate = driver.find_element_by_tag_name(tag)
        # return the information
        yield locate.text

    except(NoSuchElementException):
        yield print('Tag not found: {i}'.format(tag))


def find_tags(address):
    """ Takes the address and passes it to the <generator_search()>.
        After that, it takes the text to a dictionary with format:
        {tag: information} """

    tags = ['Point', 'Address']
    dictionary = {}
    for i in tags:
        x = generator_search(i, address)
        dictionary.update({i: next(x)})

    return dictionary


""" using the <find_tags[]> i can access the data insed of it"""

# x = find_tags(test)
# print(x['Point'])


def calc_distance(local2):
    """ calc distance in km, de default local1 will be mkad """
    take_point = find_tags(local2)
    result = distance.distance(MKAD, take_point['Point'])
    return result


x = calc_distance(test)
print(x)


def is_inside_mkad():
    # look in the xml if is inside the mkad
    is_in_mkad = driver.find_element_by_id('')
