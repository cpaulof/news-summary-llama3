import unittest
import os, sys

print(os.getcwd())

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
    
    def test_get_processed(self):
        utils.update(1, "summaryyyyyy", self.conn)
        utils.update(3, "summaryyyyyy", self.conn)
        utils.update(4, "summaryyyyyy", self.conn)
        utils.update(5, "summaryyyyyy", self.conn)
        rows = utils.get_processed(self.conn, 2, 1)
        # rows should contain rows 3 and 4
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0][0], 3)
        self.assertEqual(rows[1][0], 4)

    def test_get_single(self):
       row = utils.get_single(1, self.conn)
       expected_url = 'https://www.google.com/news'
       self.assertEqual(row[1], expected_url)
    
    def test_insert(self):
        test_url = "http://test.news.com"
        utils.insert(test_url, "source-news", "Title A", '2024-05-02 21:55:31', self.conn)

        row = utils.get_single(6, self.conn)
        self.assertEqual(row[1], test_url)

        ## test unique constrain violation
        self.assertRaises(sqlite3.IntegrityError, utils.insert, test_url, "source-news", "Title A", '2024-05-02 21:55:31',  self.conn)
        

    
    def test_update(self):
        row = utils.get_single(1, self.conn)
        self.assertEqual(row[6], 0) # assure processed column is False (0) before update

        utils.update(1, "summaryyyyyy", self.conn)

        row = utils.get_single(1, self.conn)
        self.assertEqual(row[6], 1) # assure the update happened
        self.assertIsNotNone(row[5]) # assure sql trigger also works

if __name__ == '__main__':
    sys.argv.append('-v')
    unittest.main()