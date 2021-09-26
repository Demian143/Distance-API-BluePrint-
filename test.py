import unittest
from scrapper import search_soup, calc_distance
import time

DICTIONARY = {'Point': '37.842762 55.774558',
              'Address': 'RURussia, Moscow, MKAD, 1st kilometre, inner sidecountryRussiaprovinceTsentralny federalny okrugprovinceMoscowlocalityMoscowstreetMKAD, 1st kilometre, inner side'}
LONGLAT = '37.842762, 55.774558'
INSIDE_MKAD = "Your address is inside MKAD, there's no need to calculate the distance."


class TestCase(unittest.TestCase):

    def test_search(self):
        self.assertEqual(search_soup(LONGLAT), DICTIONARY)
        time.sleep(5)
        self.assertEqual(calc_distance(LONGLAT), INSIDE_MKAD)


if __name__ == '__main__':
    unittest.main()
