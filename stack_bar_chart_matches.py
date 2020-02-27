from collections import Counter
from matplotlib import pyplot as plt

def team_with_matches_and_year(matches):
    '''To have team with count of matches along with year  '''

    season_winner_tuple_list = []
    teams = set()
    seasons = set()

    for match in matches:
        season_winner_tuple_list.append((match['season'], match['winner']))
        if match['winner'] != '':
            teams.add(match['winner'])
        seasons.add(match['season'])

    seasons = sorted(seasons)
    teams = sorted(teams)

    print(seasons)
    print(teams)

    count_season_winner_tuple_list = Counter(season_winner_tuple_list)
    season_having_list_wins = {season: [0]*len(teams) for season in seasons}

    for season, team in count_season_winner_tuple_list:
        if team != '':
            season_having_list_wins[season][teams.index(team)] = count_season_winner_tuple_list[(season, team)]

    print(season_having_list_wins)
    return season_having_list_wins, teams, seasons

def plot_team_with_matches_and_year(season_having_list_wins, teams, seasons):
    '''To plot the stacked bar chart '''

    loop_stop_var = 0

    while loop_stop_var < len(teams):
        top_array_values = []

        if loop_stop_var == 0:
            for season in seasons:
                top_array_values.append(season_having_list_wins[season][loop_stop_var])

            bottom_sum_array = top_array_values
            plt.bar(seasons, top_array_values, align='center', label=teams[loop_stop_var])

        else:
            for season in seasons:
                top_array_values.append(season_having_list_wins[season][loop_stop_var])

            plt.bar(seasons, top_array_values, bottom=bottom_sum_array, align='center', label=teams[loop_stop_var])
            bottom_sum_array = [sum(stack_sum) for stack_sum in zip(top_array_values, bottom_sum_array)]

        loop_stop_var += 1


    plt.xlabel("Year")
    plt.ylabel("Number of matches")
    plt.title("Python: Part 1 - Exercise 2 - Matches won of all teams over all the years of IPL")
    plt.legend(ncol=2, loc=1)
    plt.show()

def compute_and_plot_stack_bar_chart_matches(matches):
    '''To compute and plot stack bar chart '''

    season_having_list_wins, teams, seasons = team_with_matches_and_year(matches)
    plot_team_with_matches_and_year(season_having_list_wins, teams, seasons)
