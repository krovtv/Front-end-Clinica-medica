import sqlite3


def __ddl_comands():
    with open("./sql/ddl.sql", "r") as sql:
        return sql.read()

    


with sqlite3.connect("uniruymed.db", check_same_thread=False) as conn:
    conn.executescript(__ddl_comands())
    cursor = conn.cursor()
    