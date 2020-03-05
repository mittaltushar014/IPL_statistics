import matplotlib.pyplot as plt


def team_and_winning_matches_played_func(matches):
    '''For percent of matches played by team
       Return type: Dictionary
    '''

    team_matches_dict = dict()

    for match in matches:
        if match['winner']!="":

            if match['winner'] in team_matches_dict:
                team_matches_dict[match['winner']] += 1
            
            else:
                team_matches_dict[match['winner']] = 1

    print(team_matches_dict)
    return team_matches_dict



def plot_team_and_winning_matches_played(team_and_matches_played):
    '''Plotting percent of winning matches '''

    plt.axis("equal")
    plt.pie(team_and_matches_played.values(), labels=team_and_matches_played.keys(),
            radius=1.1, autopct='%0.2f%%')
    plt.title("Python: Part 1 - Exercise 5 - Percentage of matches won from 2008 to 2017")
    plt.show()


def compute_and_plot_total_match_in_percent_story(matches):
    '''For computing and plotting '''

    team_and_winning_matches_played = team_and_winning_matches_played_func(matches)
    plot_team_and_winning_matches_played(team_and_winning_matches_played)
