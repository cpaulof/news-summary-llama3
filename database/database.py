import sqlite3
import os

from . import utils
import config


class Database:
    def __init__(self, sql_path=config.SQL_FILE, db_path=config.DATABASE_FILE):
        exists = os.path.exists(db_path)
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        if not exists:
            utils.execute_script_file(sql_path, self.conn)
    
    def add_news(self, url, source, title, published):
        #'https://www.google.com/news', 'google news', 'titulo A', '2024-05-02 21:55:31'
        try: 
            utils.insert(url, source, title, published, self.conn)
            return True
        except sqlite3.IntegrityError:
            return False
    
    def add_summary(self, id, summary):
        utils.update(id, summary, self.conn)
    
    def get_unprocessed_urls(self):
        return utils.get_unprocessed(self.conn)
    
    def get_processed_urls(self, amount, page):
        return utils.get_processed(self.conn, amount, page)
    
    def get_last_unprocessed_url(self):
        r = utils.get_unprocessed(self.conn, single=True)
        if len(r) != 1: return None
        return r[0]

