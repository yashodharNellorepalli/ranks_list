import mysql.connector as mysql_connector

from .general import get_config_value


def get_mysql_connection():
    return mysql_connector.connect(
        user=get_config_value('MASTER_MYSQL_DATABASE_USER'),
        password=get_config_value('MASTER_MYSQL_DATABASE_PASSWORD'),
        host=get_config_value('MASTER_MYSQL_DATABASE_HOST'),
        database=get_config_value('MASTER_MYSQL_DATABASE_DB')
    )


def close_mysql_connection(mysql_conn):
    mysql_conn.close()
