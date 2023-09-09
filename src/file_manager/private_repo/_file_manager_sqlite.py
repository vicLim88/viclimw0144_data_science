import pandas as pd
import sqlite3
import sys
import traceback

from ..public.file_manager_base import file_manager_base


class FileManagerSQLite(file_manager_base):

    def __init__(self, db_file: str):
        self.db_file = db_file

    def convert_to_dataframe(self, **kwargs):
        # ToDo : Try-Catch the kwargs
        table_name: str = kwargs.get("table_name", "")
        query: str = f"SELECT * FROM {table_name}"
        conn = sqlite3.connect(self.db_file)

        try:
            return pd.read_sql(query, conn)

        # ToDo : Incorporate exception
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        finally:
            conn.close()
