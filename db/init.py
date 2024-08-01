import sqlite3
from sqlite3 import Error
import threading





class DataBaseConn:
    _instance = None
    _connection_per_thread = {}

    def __new__(cls, db_file):
        if cls._instance is None:
            cls._instance = super(DataBaseConn, cls).__new__(cls)
            cls._instance._db_file = db_file
            cls._instance._initialized = False
        else:
            pass
        return cls._instance

    def __init__(self, db_file):
        if not self._initialized:
            self._initialized = True
            self.db_file = db_file

    def _connect_to_db(self):
        """Create a database connection to the SQLite database for the current thread."""
        thread_id = threading.get_ident()
        if thread_id not in self._connection_per_thread:
            try:
                connection = sqlite3.connect(self.db_file)
                self._connection_per_thread[thread_id] = connection

            except Error as e:
                pass
                

    def get_connection(self):
        """Return the database connection for the current thread."""
        thread_id = threading.get_ident()
        if thread_id not in self._connection_per_thread:
            self._connect_to_db()
        return self._connection_per_thread[thread_id]

    def close_connection(self):
        """Close the database connection for the current thread."""
        thread_id = threading.get_ident()
        connection = self._connection_per_thread.get(thread_id)
        if connection:
            connection.close()
            del self._connection_per_thread[thread_id]

    def fetch_query(self, query):
        connection = self.get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            
            return [dict(zip(column_names, row)) for row in rows]
        
        except Error as e:
            return None



def read_sql_script(path):
    with open(path, 'r') as file:
        return file.read()