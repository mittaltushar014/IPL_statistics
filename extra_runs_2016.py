import matplotlib.pyplot as plt


def extra_runs_per_team(matches, deliveries):
    """To calculate extra runs per team """

    runs_dict = dict()
    match_id = [int(match['id']) for match in matches if match['season'] == '2016']

    for delivery in deliveries:
        if int(delivery['match_id']) in match_id and delivery['is_super_over'] == '0':
            if delivery['bowling_team'] in runs_dict:
                runs_dict[delivery['bowling_team']] += int(delivery['extra_runs'])
            else:
                runs_dict[delivery['bowling_team']] = int(delivery['extra_runs'])

    print(runs_dict)
    return runs_dict

def plot_extra_runs_per_team(extra_runs_with_team):
    '''To plot extra runs per team '''

    plt.bar(extra_runs_with_team.keys(), extra_runs_with_team.values())
    plt.xlabel("Team")
    plt.ylabel("Extra runs")
    plt.title("Python: Part 1 - Exercise 3 - Extra runs per team for 2016",)
    plt.xticks(fontsize=10, rotation=10)
    plt.show()

def compute_and_plot_extra_runs_2016(matches, deliveries):
    '''To compute and plot extra runs for 2016 '''

    extra_runs_with_team = extra_runs_per_team(matches, deliveries)
    plot_extra_runs_per_team(extra_runs_with_team)
    