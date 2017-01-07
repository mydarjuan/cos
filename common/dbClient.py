import sqlite3


def get_conn():
    conn = sqlite3.connect('/var/root/PycharmProjects/dcms-python/dcms.db')
    return conn


def add_company(id):
    conn = get_conn()
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (id, 'Paul', 32, 'California', 20000.00 )")

    conn.commit()
    conn.close()

    return True


def get_company():
    conn = get_conn()
    cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
    data = []
    for item in cursor:
        data.append(item)
    cursor.close()
    conn.close()
    return data