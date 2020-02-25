import unittest
import sys
import os
import csv

sys.path.append(os.getcwd() + '/..')
from extra_runs_2016 import extra_runs_per_team

def extract_matches():
    data_file=open('mock_matches.csv','r')
    match_file=csv.DictReader(data_file)
    return match_file

def extract_deliveries():
    data_file=open('mock_deliveries.csv','r')
    deliveries_file=csv.DictReader(data_file)
    return deliveries_file


class TestIPL(unittest.TestCase):

    def test_extra_runs_2016(self):
        test_dict = {'Delhi Daredevils': 1, 'Mumbai Indians': 4}
        self.assertEqual(extra_runs_per_team(extract_matches(), extract_deliveries()), test_dict)


if __name__ == '__main__':
    unittest.main()
