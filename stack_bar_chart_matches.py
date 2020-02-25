from collections import Counter
from matplotlib import pyplot as plt

def team_with_matches_and_year(matches):
    season_winner_tuple_list = []
    teams=set()
    seasons=set()

    for row in matches:
        season_winner_tuple_list.append((row['season'],row['winner']))
        if row['winner'] != '':
            teams.add(row['winner'])
        seasons.add(row['season'])

    seasons=sorted(seasons)
    teams=sorted(teams)

    count_season_winner_tuple_list=Counter(season_winner_tuple_list)
    season_having_list_wins={season:[0]*len(teams) for season in seasons}

    for season,team in count_season_winner_tuple_list:
        if team!='':
            season_having_list_wins[season][teams.index(team)]=count_season_winner_tuple_list[(season,team)]

    print (season_having_list_wins)
    return season_having_list_wins,teams,seasons

def plot_team_with_matches_and_year(season_having_list_wins,teams,seasons):
    loop_var=0

    while loop_var<len(teams):
        nth_index_values=[]
      
        if loop_var==0:
            for season in seasons:
                nth_index_values.append(season_having_list_wins[season][loop_var])

            bottom_add_list=nth_index_values
            plt.bar(seasons,nth_index_values,align='center',label=teams[loop_var])
      
        else:
            for season in seasons:
                nth_index_values.append(season_having_list_wins[season][loop_var])

            plt.bar(seasons,nth_index_values,bottom=bottom_add_list,align='center',label=teams[loop_var])
            bottom_add_list=[sum(stack_sum) for stack_sum in zip(nth_index_values,bottom_add_list)]

        loop_var+=1


    plt.xlabel("Year")
    plt.ylabel("Number of matches")
    plt.title("Python: Part 1 - Exercise 2 - Matches won of all teams over all the years of IPL")
    plt.legend(ncol=2,loc=1)
    plt.show()

def compute_and_plot_stack_bar_chart_matches(matches):
    season_having_list_wins,teams,seasons = team_with_matches_and_year(matches)
    plot_team_with_matches_and_year(season_having_list_wins,teams,seasons)