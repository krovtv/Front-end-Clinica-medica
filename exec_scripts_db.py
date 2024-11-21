import sqlite3


def ddl():
    with open("./sql/ddl.sql", "r", encoding='utf-8') as sql:
        return sql.read()
def pre_inserts_sql():
    with open("./sql/pre-inserts.sql", "r", encoding='utf-8') as sql:
        return sql.read()

    


with sqlite3.connect("uniruymed.db") as conn:
    conn.executescript(ddl())
    conn.executescript(pre_inserts_sql())

print("Scripts executados")