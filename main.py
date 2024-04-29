import sqlite3

import utils


DATABASE_FILE = './db.sqlite'
SQL_FILE = './data/database.sql'


class Database:
    def __init__(self, sql_path=SQL_FILE, db_path=DATABASE_FILE):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        utils.execute_script_file(sql_path, self.cursor)
    
    def add_news(self, url):
        utils.insert(url, self.cursor)
        




