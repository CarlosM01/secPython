import sqlite3

def create_database():
    con = sqlite3.connect("ejercicio.db")
    cur = con.cursor()