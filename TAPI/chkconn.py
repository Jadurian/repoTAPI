import os
import pandas as pd
import zipfile
import pyodbc
import requests
import io
from datetime import datetime, timedelta
import sqlalchemy

server = 'DARCCVWSQL19'
#server = 'DESKTOP-37ESKFT\SQLEXPRESS'
database = 'TAPI'
tabla = 'DiarioTest'
connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'

try:
    # Intentar establecer la conexión
    connection = pyodbc.connect(connection_string)
 
    # Si no hay errores, la conexión se ha establecido correctamente
    print("Conexión exitosa a la base de datos SQL Server.")
 
    # Cerrar la conexión
    connection.close()
except pyodbc.Error as e:
    # Manejar los errores de conexión
    print(f"Error al conectar a la base de datos: {e}")