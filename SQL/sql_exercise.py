import psycopg2

connection=psycopg2.connect(database="ipldatabase",
                            user="postgres",
                            host="127.0.0.1",
                            password="mountblue",
                            port="5432"
                            )



def fetch_query_data(query):
    cur = connection.cursor()
    cur.execute(query)
    query_data = cur.fetchall()
    cur.close()
    return query_data



def matches_played_per_year():
    query = "SELECT DISTINCT season, COUNT(season) FROM iplschema.matches GROUP BY season;"
    query_output = fetch_query_data(query)
    return query_output


def year_with_team_and_matches():
    query = "SELECT season, winner, COUNT(winner) FROM iplschema.matches GROUP BY season, winner \
            ORDER BY season, winner"
    query_output = fetch_query_data(query)
    return query_output


def extra_runs_2016():
    query = "SELECT DISTINCT bowling_team, SUM(extra_runs) \
             FROM iplschema.deliveries WHERE match_id \
             IN (SELECT id FROM iplschema.matches WHERE season=2016) \
             AND is_super_over=0 GROUP BY bowling_team;"
             
    query_output = fetch_query_data(query)
    return query_output


def bowler_econony():
    
    query = "SELECT DISTINCT bowler, ((SUM(total_runs-(bye_runs+legbye_runs))*6.0)/(count(CASE WHEN (noball_runs=0 AND wide_runs=0) THEN 1 ELSE NULL END))) AS Economy \
            FROM iplschema.deliveries WHERE match_id IN (SELECT id FROM iplschema.matches WHERE season=2015) \
            AND is_super_over=0 GROUP BY bowler ORDER BY Economy LIMIT 10;"
    query_output = fetch_query_data(query)
    return query_output    


def total_matches_won():
    query = "SELECT winner,COUNT(winner) AS Matches_Won FROM iplschema.matches GROUP BY winner;"
    query_output = fetch_query_data(query)
    return query_output


print(matches_played_per_year())
print("\n")
print(year_with_team_and_matches())
print("\n")
print(extra_runs_2016())
print("\n")
print(bowler_econony())
print("\n")
print(total_matches_won())


connection.close()

