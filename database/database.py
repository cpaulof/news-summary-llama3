import sqlite3

import database.utils as utils


DATABASE_FILE = './database/db.sqlite'
SQL_FILE = './data/database.sql'


class Database:
    def __init__(self, sql_path=SQL_FILE, db_path=DATABASE_FILE):
        self.conn = sqlite3.connect(db_path)
        utils.execute_script_file(sql_path, self.conn)
    
    def add_news(self, url):
        utils.insert(url, self.conn)
    
    def add_summary(self, id, summary):
        utils.update(id, summary, self.conn)
    
    def get_unprocessed_urls(self):
        return utils.get_unprocessed(self.conn)
    
    def get_processed_urls(self, amount, page):
        return utils.get_processed(self.conn, amount, page)
