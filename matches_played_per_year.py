import matplotlib.pyplot as plt

def matches_played_per_year_func(matches):
    """To return the data of matches played per year """

    matches_dict = dict()

    for match in matches:
        if match['season'] in matches_dict:
            matches_dict[match['season']] += 1
        else:
            matches_dict[match['season']] = 1

    print(matches_dict)
    return matches_dict


def plot_matches_played_per_year(matches_per_year):
    """To plot matches played per year """

    plt.bar(matches_per_year.keys(), matches_per_year.values())
    plt.xlabel("Year")
    plt.ylabel("Number of matches played")
    plt.title("Python: Part 1 - Exercise 1 - Number of matches played per year")
    plt.show()


def compute_and_plot_matches_played_per_year(matches):
    """To compute and plot matches played per year """

    matches_per_year = matches_played_per_year_func(matches)
    plot_matches_played_per_year(matches_per_year)
