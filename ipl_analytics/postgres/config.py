from configparser import ConfigParser
config = ConfigParser()
config['database'] = {
    'database': "ipl_db",
    'user': "postgres",
    'host': "127.0.0.1",
    'port': "5432",
    'key' : "--enter--key-here--",
    'encoded_ciphertext' : "c2MAAl0+ZypGvob734Exg20mqBMRTr6aVg2acAB+b2vFqVUySTYF4C4zwlswrBWU7C/aDcoQuiEhqGi0dzr+g42Eo7IwZENZIcgRvP0="
}
with open('./config.ini', 'w') as f:
    config.write(f)
