import psycopg2
from configparser import ConfigParser
from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode

parser=ConfigParser()
parser.read("config.ini")

def decrypt_password():
    key = parser.get('database','key')
    encoded_ciphertext = parser.get('database','encoded_ciphertext')
    cipher = b64decode(encoded_ciphertext)
    decrypted_password_plaintext = decrypt(key, cipher)
    return decrypted_password_plaintext


connection=psycopg2.connect(database=parser.get('database', 'database'),
                            user=parser.get('database', 'user'),
                            host=parser.get('database', 'host'),
                            password=decrypt_password(),
                            port=parser.get('database', 'port')
                            )


def fetch_query_data(query):
    cur = connection.cursor()
    cur.execute(query)
    query_data = cur.fetchall()
    cur.close()
    return query_data



def matches_played_per_year_sql(data):
    """ Returning matches played per year 
        Return type : List of tuples
    """
    if data == True:
        table = "iplschema.matches"
    else:
        table = "iplschema.mock_matches"


    query = "SELECT DISTINCT season, COUNT(season) FROM {} GROUP BY season;".format(table)
    query_output = fetch_query_data(query)
    
    for data in query_output:
        print(data[0],int(data[1]))

    return query_output


def year_with_team_and_matches_sql(data):
    """ Returning Year with team and number of matches won 
        Return type : List of tuples
    """
    if data == True:
        table = "iplschema.matches"
    else:
        table = "iplschema.mock_matches"

    query = "SELECT season, winner, COUNT(winner) FROM {} WHERE winner IS NOT NULL GROUP BY season, winner \
            ORDER BY season, winner".format(table)
    query_output = fetch_query_data(query)

    for data in query_output:
        print(data[0],data[1],int(data[2]))

    return query_output


def extra_runs_2016_sql(data):
    """ Returning Extra runs scored per team
        Return type : List of tuples
    """

    if data == True:
        table1 = "iplschema.deliveries"
        table2 = "iplschema.matches"
    else:
        table1 = "iplschema.mock_deliveries"
        table2 = "iplschema.mock_matches"

    query = "SELECT DISTINCT bowling_team, SUM(extra_runs) \
             FROM {} WHERE match_id \
             IN (SELECT id FROM {} WHERE season=2016) \
             AND is_super_over=0 GROUP BY bowling_team;".format(table1,table2)
             
    query_output = fetch_query_data(query)
    
    for data in query_output:
        print(data[0],int(data[1]))

    return query_output


def bowler_economy_sql(data):
    """ Returning bowler and his economy
        Return type : List of tuples
    """
    if data == True:
        table1 = "iplschema.deliveries"
        table2 = "iplschema.matches"
    else:
        table1 = "iplschema.mock_deliveries"
        table2 = "iplschema.mock_matches"
    
    query = "SELECT DISTINCT bowler, ((SUM(total_runs-(bye_runs+legbye_runs))*6.0)/(count(CASE WHEN (noball_runs=0 AND wide_runs=0) THEN 1 ELSE NULL END))) AS Economy \
            FROM {} WHERE match_id IN (SELECT id FROM {} WHERE season=2015) \
            AND is_super_over=0 GROUP BY bowler ORDER BY Economy LIMIT 10;".format(table1,table2)
    query_output = fetch_query_data(query)

    query_list=list()

    for data in query_output:
        print(data[0],float(data[1]))
        query_list.append((data[0],float(data[1])))
   
    return query_list
    

def total_matches_won_sql(data):
    """ Returning total matches won per team
        Return type : List of tuples
    """

    if data == True:
        table = "iplschema.matches"
    else:
        table = "iplschema.mock_matches"

    query = "SELECT winner,COUNT(winner) AS Matches_Won FROM {}  WHERE winner is NOT NULL GROUP BY winner;".format(table)
    query_output = fetch_query_data(query)

    for data in query_output:
        print(data[0],int(data[1]))

    return query_output

matches_played_per_year_sql(True)
print("\n")
year_with_team_and_matches_sql(True)
print("\n")
extra_runs_2016_sql(True)
print("\n")
bowler_economy_sql(True)
print("\n")
total_matches_won_sql(True)


