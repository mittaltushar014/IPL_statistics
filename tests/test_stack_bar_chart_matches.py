import unittest
import sys
import os
import csv

sys.path.insert(2,os.path.join(os.getcwd(),'..'))
sys.path.insert(3,os.path.join(os.getcwd(),'../SQL/'))

from stack_bar_chart_matches import team_with_matches_and_year
from sql_exercise import *

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
        test_sql_output=[(2008, 'Kolkata Knight Riders', 1L), (2009, 'Mumbai Indians', 1L),
                         (2010, 'Kolkata Knight Riders', 1L), (2011, 'Chennai Super Kings', 1L),
                         (2011, 'Rajasthan Royals', 1L), (2015, 'Chennai Super Kings', 1L),
                         (2015, 'Kolkata Knight Riders', 1L), (2016, 'Kolkata Knight Riders', 1L),
                         (2016, 'Rising Pune Supergiant', 1L), (2017, 'Sunrisers Hyderabad', 1L)]             
        match_dict = team_with_matches_and_year(extract_matches())[0]
        self.assertEqual(match_dict, test_dict)
        self.assertEqual(year_with_team_and_matches_sql(False),test_sql_output)


if __name__ == '__main__':
    unittest.main()
