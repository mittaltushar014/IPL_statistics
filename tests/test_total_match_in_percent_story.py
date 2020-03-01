import unittest
import sys
import os
import csv

sys.path.insert(2,os.path.join(os.getcwd(),'..'))

from total_match_in_percent_story import team_and_winning_matches_played_func

def extract_matches():
    '''For extracting matches '''

    data_file = open('mock_matches.csv', 'r')
    match_file = csv.DictReader(data_file)
    return match_file


class TestIPL(unittest.TestCase):
    '''For testing IPL '''

    def test_total_match_in_percent_story(self):
        '''For testing match percent of team '''

        test_dict = {'Kolkata Knight Riders': 4, 'Chennai Super Kings': 2,
                     'Rising Pune Supergiant': 1, 'Sunrisers Hyderabad': 1,
                     'Rajasthan Royals': 1, 'Mumbai Indians': 1}
        self.assertEqual(team_and_winning_matches_played_func(extract_matches()), test_dict)


if __name__ == '__main__':
    unittest.main()
