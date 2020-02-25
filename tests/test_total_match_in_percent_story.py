import unittest
import sys
import os
import csv

sys.path.append(os.getcwd() + '/..')
from total_match_in_percent_story import team_and_winning_matches_played_func

def extract_matches():
    data_file=open('mock_matches.csv','r')
    match_file=csv.DictReader(data_file)
    return match_file

def extract_deliveries():
    data_file=open('mock_deliveries.csv','r')
    deliveries_file=csv.DictReader(data_file)
    return deliveries_file


class TestIPL(unittest.TestCase):

    def test_total_match_in_percent_story(self):
        test_dict={'Kolkata Knight Riders': 4, 'Chennai Super Kings': 2, 'Sunrisers Hyderabad': 1, 'Rising Pune Supergiants': 1, 'Rajasthan Royals': 1, 'Mumbai Indians': 1}
        self.assertEqual(team_and_winning_matches_played_func(extract_matches()),test_dict)


if __name__ == '__main__':
    unittest.main()
