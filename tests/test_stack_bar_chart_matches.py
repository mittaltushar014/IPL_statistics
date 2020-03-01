import unittest
import sys
import os
import csv

sys.path.insert(2,os.path.join(os.getcwd(),'..'))

from stack_bar_chart_matches import team_with_matches_and_year

def extract_matches():
    '''For extracting matches '''

    data_file = open('mock_matches.csv', 'r')
    match_file = csv.DictReader(data_file)
    return match_file


class TestIPL(unittest.TestCase):
    '''For testing IPL '''

    def test_stack_bar_chart_matches(self):
        '''Testing stack bar chart '''

        test_dict = {'2009': [0, 0, 1, 0, 0, 0],
                     '2017': [0, 0, 0, 0, 0, 1],
                     '2015': [1, 1, 0, 0, 0, 0],
                     '2008': [0, 1, 0, 0, 0, 0],
                     '2016': [0, 1, 0, 0, 1, 0],
                     '2011': [1, 0, 0, 1, 0, 0],
                     '2010': [0, 1, 0, 0, 0, 0]}
        match_dict = team_with_matches_and_year(extract_matches())[0]
        self.assertEqual(match_dict, test_dict)


if __name__ == '__main__':
    unittest.main()
