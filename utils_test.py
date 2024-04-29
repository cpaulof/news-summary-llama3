import unittest
import os, sys

import sqlite3
import utils

DATABASE_FILE = './db_test.sqlite'
SQL_FILE = './data/database_test.sql'

class TestUtils(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestUtils, self).__init__(*args, **kwargs)
       
        
    def setUp(self):
        if os.path.exists(DATABASE_FILE): # delete old test database
            os.remove(DATABASE_FILE)

        self.conn = sqlite3.connect(DATABASE_FILE)
        utils.execute_script_file(SQL_FILE, self.conn)

    def tearDown(self):
        try:
            self.conn.close()
        except: pass

    def test_create_database(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM news")
        rows = cursor.fetchall()
        cursor.close()
        self.assertEqual(len(rows), 5)

    def test_get_unprocessed(self):
        rows = utils.get_unprocessed(self.conn)
        self.assertEqual(len(rows), 4)

    def test_get_single(self):
       row = utils.get_single(1, self.conn)
       expected_url = 'https://www.google.com/news'
       self.assertEqual(row[1], expected_url)

if __name__ == '__main__':
    sys.argv.append('-v')
    unittest.main()