import sqlite3
import json

class Database_manager():
    def __init__(self):
        self.db = "save_data.db"
        self.conn = sqlite3.connect(self.db)
        self.cur = self.conn.cursor()
        self.id = 0
    def create(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS save_data (
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         high_scores TEXT
                         )""")
        self.conn.commit()
    def add(self, high_scores):
        json_data = json.dumps(high_scores)
        self.cur.execute("""INSERT INTO save_data (high_scores) VALUES (?)""", (json_data,))
        self.conn.commit()
        self.id += 1

    def read(self):
        save_data = list((self.cur.execute("""SELECT * FROM save_data ORDER BY id DESC;""")).fetchone())
        save_data[1] = json.loads(save_data[1])
        return save_data
    
    def update(self, high_scores):
        json_data = json.dumps(high_scores)
        self.cur.execute("""UPDATE save_data SET high_scores = ? WHERE id = ?""", (json_data, self.id))
        self.conn.commit()
        return True
    def delete(self):
        self.cur.execute("""UPDATE save_data SET high_scores = ? WHERE id = ?""", (json.dumps({}), self.id))
        self.conn.commit()


