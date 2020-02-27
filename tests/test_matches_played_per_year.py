import unittest
import sys
import os
import csv

sys.path.insert(2,os.path.join(os.getcwd(),'..'))
#sys.path.append(os.getcwd() + '/..')

from matches_played_per_year import matches_played_per_year_func

def extract_matches():
    '''For extracting matches'''

    data_file = open('mock_matches.csv', 'r')
    match_file = csv.DictReader(data_file)
    return match_file


class TestIPL(unittest.TestCase):
    '''For testing IPL '''

    def test_matches_played_per_year(self):
        '''Testing matches played per year '''

        test_dict = {'2009': 1, '2010': 1, '2015': 2, '2017': 1, '2016': 2, '2011': 2, '2008': 1}
        self.assertEqual(matches_played_per_year_func(extract_matches()), test_dict)


if __name__ == '__main__':
    unittest.main()
