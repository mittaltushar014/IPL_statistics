import unittest
import sys
import os
import csv

sys.path.append(os.getcwd() + '/..')
from economical_bowlers_by_list import economical_bowler_with_economy


def extract_matches():
    data_file=open('mock_matches.csv','r')
    match_file=csv.DictReader(data_file)
    return match_file

def extract_deliveries():
    data_file=open('mock_deliveries.csv','r')
    deliveries_file=csv.DictReader(data_file)
    return deliveries_file


class TestIPL(unittest.TestCase):

    def test_economical_bowlers_by_list(self):
        test_dict={'UT Yadav': 7.5, 'M Morkel': 9.0, 'JA Morkel': 12.0, 'NM Coulter-Nile': 10.0, 'DJ Muthuswami': 6.0}
        self.assertEqual(economical_bowler_with_economy(extract_matches(),extract_deliveries()), test_dict)


if __name__ == '__main__':
    unittest.main()
