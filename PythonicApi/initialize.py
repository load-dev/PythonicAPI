import mysql.connector
from mysql.connector import Error
import json

class pnapi:
    def db(self, host, database, user, password, table_name, db_type='mysql'):
        if db_type.lower() != 'mysql':
            return {"status":"400", "message":"pnapi only supports MySQL for now."}
        try:
            connection = mysql.connector.connect(
                host=host,
                database=database,
                user=user,
                password=password
            )
            
            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)
                cursor.execute(f"SELECT * FROM {table_name}")
                rows = cursor.fetchall()
                
                result = {}
                for row in rows:
                    for key, value in row.items():
                        if key not in result:
                            result[key] = []
                        result[key].append(value)
                        
                cursor.close()
                connection.close()
                return result
        except Error as e:
            raise TypeError(f"[pnapi error]: Failed to connect to database: {e}")
        except Exception as ex:
            return TypeError(f"[pnapi error]: An error has occurred: {ex}")

    def login(self, dbinfo, requests_table, dbdata_table):
        if not isinstance(requests_table, list):
            raise TypeError("[pnapi error]: requests_table must be a list")
        if not isinstance(dbdata_table, list):
            raise TypeError("[pnapi error]: dbdata_table must be a list")

        try:
            for table_name in dbdata_table:
                if table_name not in dbinfo:
                    return {"status":"400", "message":"This data table does not exist."}
                for request in requests_table:
                    if request in dbinfo[table_name]:
                        return {"status": "100", "message": None}
                    else:
                        return {"status": "101", "message": "This data are not in the database!"}
        except Exception as e:
            raise Exception(f"[pnapi error]: {e}")
        
    def request(self, server_func, return_data="normal"):
        if not callable(server_func):
            return {"status":"400", "message":"[pnapi error]: Server function must be a function"}
        
        try:
            server_func()
            return {"status":"100", "message":None}
        except Exception as e:
            return {"status":"300", "message":f"{e}"}