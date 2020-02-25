import matplotlib.pyplot as plt

def economical_bowler_with_economy(matches,deliveries):
    """
    To calculate economy of bowlers
    """

    bowler_dict = dict()
    match_id=[int(row['id']) for row in matches if int(row['season']) == 2015]  
    
    
    for row in deliveries:
        if int(row['match_id']) in match_id and row['is_super_over'] == '0':
            runs = int(row['total_runs']) - (int(row['bye_runs']) + int(row['legbye_runs']))
            if row['bowler'] in bowler_dict:
                bowler_dict[row['bowler']] = [bowler_dict[row['bowler']][0] + runs, bowler_dict[row['bowler']][1] + 1]
            else:
                bowler_dict[row['bowler']] = [runs, 1]

    bowler_final_dict = dict()
    final_economy=0.1
    
    for bowler, runs_and_balls in bowler_dict.items():
        final_economy = float(runs_and_balls[0]) / float((runs_and_balls[1]/6))
        bowler_final_dict[bowler] = final_economy

    print(bowler_final_dict)
    return bowler_final_dict


def plot_economical_bowler_and_economy(economical_bowler_and_economy):
    """
    To plot economy of bowler
    """

    bowler=[]
    economy=[]
    loop_stop_var=1

    for bowler_man, bowler_eco in sorted(economical_bowler_and_economy.items(), key= lambda x: x[1]):
        bowler.append(bowler_man)
        economy.append(bowler_eco)
        loop_stop_var += 1
        if (loop_stop_var > 3):
            break

    plt.bar(bowler, economy)
    plt.xlabel("Bowler")
    plt.ylabel("Economy")
    plt.title("Python: Part 1 - Exercise 4 - Bowlers and economy")
    plt.xticks(fontsize=10, rotation=10)
    plt.show()


def compute_and_plot_economical_bowlers_by_list(matches, deliveries):
    """
    To compute and plot economy of bowler
    """

    economical_bowler_and_economy = economical_bowler_with_economy(matches, deliveries)
    plot_economical_bowler_and_economy(economical_bowler_and_economy)