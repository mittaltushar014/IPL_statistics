from configparser import ConfigParser
config = ConfigParser()
config['database'] = {
    'database': "ipl_db",
    'user': "postgres",
    'host': "127.0.0.1",
    'port': "5432",
    'key' : "--enter--key-here--",
}
with open('./config.ini', 'w') as f:
    config.write(f)
