import unittest
import sys
import os
import csv

sys.path.insert(2,os.path.join(os.getcwd(),'..'))

from extra_runs_2016 import extra_runs_per_team

def extract_matches():
    '''For extracting matches '''

    data_file = open('mock_matches.csv', 'r')
    match_file = csv.DictReader(data_file)
    return match_file

def extract_deliveries():
    '''For extracting deliveries '''

    data_file = open('mock_deliveries.csv', 'r')
    deliveries_file = csv.DictReader(data_file)
    return deliveries_file


class TestIPL(unittest.TestCase):
    '''For testing IPL '''

    def test_extra_runs_2016(self):
        '''Testing extra runs '''

        test_dict = {'Kolkata Knight Riders': 1, 'Rising Pune Supergiant': 4}
        self.assertEqual(extra_runs_per_team(extract_matches(), extract_deliveries()), test_dict)


if __name__ == '__main__':
    unittest.main()
