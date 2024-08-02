import unittest
import threading
import sqlite3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.init import DataBaseConn, read_sql_script

class TestDataBaseConn(unittest.TestCase):
    def setUp(self):
        self.db_file = "./db/test.db"
        self.db_conn = DataBaseConn(self.db_file)

    def tearDown(self):
        self.db_conn.close_connection()

    def test_singleton_instance(self):
        db_conn1 = DataBaseConn(self.db_file)
        db_conn2 = DataBaseConn(self.db_file)
        self.assertIs(db_conn1, db_conn2)

    def test_connect_to_db(self):
        self.db_conn._connect_to_db()
        thread_id = threading.get_ident()
        self.assertIn(thread_id, self.db_conn._connection_per_thread)
        self.assertIsInstance(self.db_conn._connection_per_thread[thread_id], sqlite3.Connection)

    def test_get_connection(self):
        connection = self.db_conn.get_connection()
        thread_id = threading.get_ident()
        self.assertEqual(connection, self.db_conn._connection_per_thread[thread_id])

    def test_close_connection(self):
        self.db_conn.get_connection()
        self.db_conn.close_connection()
        thread_id = threading.get_ident()
        self.assertNotIn(thread_id, self.db_conn._connection_per_thread)

    def test_fetch_query(self):
        query = "SELECT * FROM task WHERE Id = 1"
        result = self.db_conn.fetch_query(query)
        expected_result = [{
            'Id': 1, 'Title': 'Meeting with team', 'Datetime': '2024-07-21 10:00:00',
            'Message': 'Discuss project updates', 'User': 'Jorge Villa', 'Guess': 'Yes',
            'Alarm': 'None', 'LocationId': 1, 'PriorityId': 1
        }]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
