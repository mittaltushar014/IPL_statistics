import matplotlib.pyplot as plt
from collections import OrderedDict

def economical_bowler_with_economy(matches, deliveries):
    """To calculate economy of bowlers 
       Return type: Dictionary
    """

    bowler_dict = dict()
    match_id = [int(match['id']) for match in matches if match['season'] == '2015']


    for delivery in deliveries:

        if int(delivery['match_id']) in match_id and delivery['is_super_over'] == '0':
            runs = int(delivery['total_runs']) - (int(delivery['bye_runs']) + int(delivery['legbye_runs']))

            if delivery['bowler'] in bowler_dict.keys():
                bowler_dict[delivery['bowler']][0] += runs
                if delivery['wide_runs'] == '0' and delivery['noball_runs'] == '0':
                    bowler_dict[delivery['bowler']][1] += 1

            else:
                bowler_dict[delivery['bowler']] = [runs, 0]
                if delivery['wide_runs'] == '0' and delivery['noball_runs'] == '0':
                    bowler_dict[delivery['bowler']][1] = 1


    bowler_final_dict = dict()
    final_economy = 0.1

    for bowler, runs_and_balls in bowler_dict.items():
        final_economy = (float(runs_and_balls[0]) / float(runs_and_balls[1]))*6
        bowler_final_dict[bowler] = final_economy

    print(bowler_final_dict)
    return bowler_final_dict


def plot_economical_bowler_and_economy(economical_bowler_and_economy):
    
    economical_bowler_ordered_dict=OrderedDict()

    for item in sorted(economical_bowler_and_economy.items(), key= lambda item : item[1]):
        economical_bowler_ordered_dict[item[0]]=item[1]
      

    plt.bar(economical_bowler_ordered_dict.keys()[0:10], economical_bowler_ordered_dict.values()[0:10])
    plt.xlabel("Bowler")
    plt.ylabel("Economy")
    plt.title("Python: Part 1 - Exercise 4 - Bowlers and economy")
    plt.xticks(fontsize=10, rotation=10)
    plt.show()


def compute_and_plot_economical_bowlers_by_list(matches, deliveries):
    """To compute and plot economy of bowler """

    economical_bowler_and_economy = economical_bowler_with_economy(matches, deliveries)
    plot_economical_bowler_and_economy(economical_bowler_and_economy)

