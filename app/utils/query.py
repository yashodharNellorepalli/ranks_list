def get_mysql_results(mysql_conn, query):
    try:
        cursor = mysql_conn.cursor()
        cursor.execute(query)
        rows_data = cursor.fetchall()
        fields = list(map(lambda x: str(x[0]), cursor.description))
        data = map(lambda row: dict(zip(fields, row)), rows_data)
        cursor.close()

        return list(data)
    except Exception:
        return list()


def insert_mysql_rows(mysql_conn, query):
    try:
        cursor = mysql_conn.cursor()
        cursor.execute(query)
        mysql_conn.commit()
        cursor.close()

        return True
    except Exception:
        return False
