import psycopg2

hostname = 'localhost'
database = 'musicapp'
username = 'postgres'
pwd = 'Loving76'
port_id = 5432


conn = psycopg2.connect(
            hostname = hostname,
            dbname = database, 
            user = username,
            password = pwd, 
            port = port_id)


conn.close()




















