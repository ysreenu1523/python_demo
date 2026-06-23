import os

def mysql_conn():
    USER=os.getenv("MYSQL_USER")
    PASSWORD=os.getenv("MYSQL_PASSWORD")
    HOST=os.getenv("MYSQL_HOST")
    PORT=os.getenv("MYSQL_PORT")
    DATABASE=os.getenv("MYSQL_SCHEMA")

    mysql_connection_string = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

    return mysql_connection_string
