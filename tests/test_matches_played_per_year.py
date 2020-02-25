import unittest
import sys
import os
import csv


sys.path.append(os.getcwd() + '/..')
from matches_played_per_year import matches_played_per_year_func


def extract_matches():
    data_file=open('mock_matches.csv','r')
    match_file=csv.DictReader(data_file)
    return match_file


class TestIPL(unittest.TestCase):

    def test_matches_played_per_year(self):
        test_dict = {
            '2009': 1,
            '2010': 1,
            '2015': 2,
            '2017': 1,
            '2016': 2,
            '2011': 2,
            '2008': 1}
        self.assertEqual(matches_played_per_year_func(extract_matches()), test_dict)


if __name__ == '__main__':
    unittest.main()
