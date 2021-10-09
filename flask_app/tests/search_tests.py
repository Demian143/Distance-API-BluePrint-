import unittest
from flask_app.blueprints.distance_api.scrapper import Search

soup_response = {'Point': '37.842762 55.774558',
                 'Address': 'RURussia, Moscow, MKAD, 1st kilometre, inner sidecountryRussiaprovinceTsentralny federalny okrugprovinceMoscowlocalityMoscowstreetMKAD, 1st kilometre, inner side'}
inside_mkad = "Your address is inside MKAD, there's no need to calculate the distance."
coordinate = (37.842762, 55.774558)


class TestSearch(unittest.TestCase):
    def test_search_soup(self):
        soup = Search.search_soup(self, coordinate)
        self.assertEqual(soup, soup_response)

    def test_calc_distance(self):
        search = Search()
        distance = search.calc_distance(coordinate)
        self.assertEqual(distance, inside_mkad)


if __name__ == '__main__':
    unittest.main()
