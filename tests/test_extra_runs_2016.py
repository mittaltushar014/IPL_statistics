import unittest
import sys
import os
import csv

sys.path.insert(2,os.path.join(os.getcwd(),'../ipl_analytics/csv/'))
sys.path.insert(3,os.path.join(os.getcwd(),'../ipl_analytics/postgres/'))

from extra_runs_2016 import extra_runs_per_team
from sql_exercise import *

def extract_matches():
    '''For extracting matches '''

    data_file = open('../data/mock_matches.csv', 'r')
    match_file = csv.DictReader(data_file)
    return match_file

def extract_deliveries():
    '''For extracting deliveries '''

    data_file = open('../data/mock_deliveries.csv', 'r')
    deliveries_file = csv.DictReader(data_file)
    return deliveries_file


class TestIPL(unittest.TestCase):
    '''For testing IPL '''

    def test_extra_runs_2016(self):
        '''Testing extra runs '''

        test_dict = {'Kolkata Knight Riders': 1, 'Rising Pune Supergiant': 4}
        
        self.assertEqual(extra_runs_per_team(extract_matches(), extract_deliveries()), test_dict)
        self.assertEqual({team:extra_runs for team, extra_runs in extra_runs_2016_sql(False)},test_dict)


if __name__ == '__main__':
    unittest.main()
