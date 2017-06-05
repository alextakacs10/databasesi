import psycopg2
import db_login


def handle_data(SQL):
    """Initiate connection -> retrieve data -> close connection"""

    try:
        db, user, pw, host = db_login.db_login_info()
        login_info = "dbname='{}' user='{}' host='{}' password='{}'".format(db, user, host, pw)
        conn = psycopg2.connect(login_info)
        cursor = conn.cursor()
        cursor.execute(SQL)
        result = cursor.fetchall()
        return result
    except psycopg2.DatabaseError:
        print("Can't connect to the server, try again.")
        abort(505)
    finally:
        if conn:
            conn.close()