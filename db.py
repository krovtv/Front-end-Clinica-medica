import sqlite3



with sqlite3.connect("uniruymed.db", check_same_thread=False) as conn:
    cursor = conn.cursor()
    