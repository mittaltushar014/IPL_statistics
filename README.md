
#### Python 2.7.17

Project for transforming raw data from IPL into graphs that will convey some meaning / analysis.

#### Instructions:

1-- Run main.py for PART 1 - Python output
2-- Run each test file in tests/ folder to test for csv and sql output testing for Part 2 - Unit testing.
3-- Run sql_exercise.py in ipl_analytics/postgres/ folder for Part 3 - SQL output.
    ( To run sql_exercise.py, obtain key from the owner of project and enter in ipl_analytics/postgres/config.ini )


#### Part 1 - Python:

Different python functions to do the following tasks.

1. Plot the number of matches played per year of all the years in IPL.
2. Plot a stacked bar chart of matches won of all teams over all the years of IPL.
3. For the year 2016 plot the extra runs conceded per team.
4. For the year 2015 plot the top economical bowlers.
5. Discussing a "Story" you want to tell with the given data. As with part 1, preparing the data structure and plot with matplotlib.


#### Part 2 - Unit Testing:

Creating our own smaller dataset - like 5 matches and 15 deliveries. Manually setting the result for the unit tests. 


#### Part 3- SQL:

Importing our test source into a Postgresql database i.e. ipl_test_db. Writing SQL queries for each of the above questions. Saving it into a text file. Using the psql prompt or pgadmin to write queries.

Now, connecting to the database from Python using the psycopg2 library
Defining separate functions which execute each query.
These functions must return the same data as your Python business logic functions, so that the corresponding plot functions can be shared between them.
Comparing the SQL output with your original Python functions' output.

Directory Structure:

.
├── data
│   ├── deliveries.csv
│   ├── matches.csv
│   ├── mock_deliveries.csv
│   └── mock_matches.csv
├── .gitignore
├── ipl_analytics
│   ├── csv
│   │   ├── economical_bowlers_by_list.py
│   │   ├── extra_runs_2016.py
│   │   ├── matches_played_per_year.py
│   │   ├── stack_bar_chart_matches.py
│   │   └── total_match_in_percent_story.py
│   └── postgres
│       ├── config.ini
│       ├── config.py
│       ├── encrypt.py
│       ├── sql_exercise.py
│       └── SQL_Python_Commands.txt
├── main.py
├── README.md
├── requirements.txt
└── tests
    ├── config.ini
    ├── test_economical_bowler_by_list.py
    ├── test_extra_runs_2016.py
    ├── test_matches_played_per_year.py
    ├── test_stack_bar_chart_matches.py
    └── test_total_match_in_percent_story.py

