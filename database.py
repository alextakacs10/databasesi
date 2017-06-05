import psycopg2
import db_login


def handle_data(query):
    """Initiate connection -> retrieve data -> close connection"""

    try:
        db, user, pw, host = db_login.db_login_info()
        login_info = "dbname='{}' user='{}' host='{}' password='{}'".format(db, user, host, pw)
        conn = psycopg2.connect(login_info)
        cursor = conn.cursor()
        cursor.execute(query)
        header = [desc[0] for desc in cursor.description]
        result = cursor.fetchall()
        return header, result
    except psycopg2.DatabaseError:
        print("Can't connect to the server, try again.")
        abort(505)
    finally:
        if conn:
            conn.close()