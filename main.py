import csv
import sys
import os

sys.path.insert(2,os.path.join(os.getcwd(),'ipl_analytics/csv'))

from matches_played_per_year import compute_and_plot_matches_played_per_year
from stack_bar_chart_matches import compute_and_plot_stack_bar_chart_matches
from extra_runs_2016 import compute_and_plot_extra_runs_2016
from economical_bowlers_by_list import compute_and_plot_economical_bowlers_by_list
from total_match_in_percent_story import compute_and_plot_total_match_in_percent_story


def extract_matches():
    '''To extract matches '''

    data_file = open('data/matches.csv', 'r')
    match_file = csv.DictReader(data_file)
    return match_file

def extract_deliveries():
    '''To extract deliveries '''

    data_file = open('data/deliveries.csv', 'r')
    deliveries_file = csv.DictReader(data_file)
    return deliveries_file


def main():
    '''To compute and plot different exercises '''

    compute_and_plot_matches_played_per_year(extract_matches())
    compute_and_plot_stack_bar_chart_matches(extract_matches())
    compute_and_plot_extra_runs_2016(extract_matches(), extract_deliveries())
    compute_and_plot_economical_bowlers_by_list(extract_matches(), extract_deliveries())
    compute_and_plot_total_match_in_percent_story(extract_matches())


if __name__ == "__main__":
    main()
