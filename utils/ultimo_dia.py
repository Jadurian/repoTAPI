import pandas as pd
import pyodbc

def ultimo_dia_tabla(tabla:str) -> str:
    server = 'DARCCVWSQL19'
    database = 'TAPI'
    connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    query = f"SELECT TOP 1 FECHA FROM {tabla} ORDER BY FECHA DESC"
    df = pd.read_sql(query, connection)
    cursor.close()
    ultimo_dia = df['FECHA'][0]
    
    return ultimo_dia