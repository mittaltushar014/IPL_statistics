import unittest
import sys
import os
import csv

sys.path.insert(2,os.path.join(os.getcwd(),'../ipl_analytics/csv/'))
sys.path.insert(3,os.path.join(os.getcwd(),'../ipl_analytics/postgres/'))

from economical_bowlers_by_list import economical_bowler_with_economy
from sql_exercise import *


def extract_matches():
    '''For extracting matches
       Return type : list of dictionary
    '''

    data_file = open('../data/mock_matches.csv', 'r')
    match_file = csv.DictReader(data_file)
    return match_file

def extract_deliveries():
    '''For extracting deliveries
       Return type : list of dictionary
    '''

    data_file = open('../data/mock_deliveries.csv', 'r')
    deliveries_file = csv.DictReader(data_file)
    return deliveries_file


class TestIPL(unittest.TestCase):
    '''For testing IPL '''

    def test_economical_bowlers_by_list(self):
        '''For testing bowlers economy '''

        test_dict = {'UT Yadav': 7.5, 'M Morkel': 6.75, 'JA Morkel': 12.0,
                     'NM Coulter-Nile': 8.571428571428571, 'DJ Muthuswami': 6.0}
              
        self.assertEqual(economical_bowler_with_economy(extract_matches(), extract_deliveries()), test_dict)
        self.assertEqual({bowler:eco for bowler, eco in bowler_economy_sql(False)},test_dict)


if __name__ == '__main__':
    unittest.main()

