import sqlite3
import os


def get_conn():
    try:
        conn = sqlite3.connect(os.path.dirname(os.path.abspath(__file__)) + '/dcms.db')
    except IOError as e:
        print(e)
    return conn


def execute_query(sql, params):
    try:
        conn = get_conn()
        cursor = conn.execute(sql, params)
    except Exception as e:
        print(e)
        data = []
        for item in cursor:
            data.append(item)
        cursor.close()
    finally:
        conn.close()
    return data


def execute_no_query(sql, params):
    try:
        conn = get_conn()
        conn.execute(sql, params)
    except Exception as e:
        print(e)
        conn.rollback()
    else:
        conn.commit()
    finally:
        conn.close()
