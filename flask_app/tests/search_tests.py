import unittest
from flask_app.blueprints.distance_api.scrapper import Search


class TestSearch(unittest.TestCase):
    INSIDE_MKAD = "Your address is inside MKAD, there's no need to calculate the distance."
    COORDINATE = (37.842762, 55.774558)
    SOUP_RESPONSE = {'Point': '37.842762 55.774558',
                     'Address': 'RURussia, Moscow, MKAD, 1st kilometre, inner sidecountryRussiaprovinceTsentralny federalny okrugprovinceMoscowlocalityMoscowstreetMKAD, 1st kilometre, inner side'}

    def test_search_soup(self):
        soup = Search.search_soup(self, TestSearch.COORDINATE)
        self.assertEqual(soup, TestSearch.SOUP_RESPONSE)

    def test_calc_distance(self):
        search = Search()
        distance = search.calc_distance(TestSearch.COORDINATE)
        self.assertEqual(distance, TestSearch.INSIDE_MKAD)


if __name__ == '__main__':
    unittest.main()
