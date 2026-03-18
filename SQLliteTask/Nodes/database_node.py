import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)

    def query(self, sql, params=()):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        return cur.fetchall()

    def execute(self, sql: str, params=()):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()
    def executemany(self, sql : str, params=()):
        cur =self.conn.cursor()
        cur.executemany(sql,params)
        self.conn.commit()
    def close(self):
        self.conn.close()
