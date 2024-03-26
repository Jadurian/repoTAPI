#codigo para capturar el último día cargado en la BBDD

import os
import pandas as pd
import zipfile
import pyodbc
import requests
import io
from datetime import datetime, timedelta
from sqlalchemy import engine
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

def ultimo_dia_sql():
    server = 'DARCCVWSQL19'
    #server = 'DESKTOP-37ESKFT\SQLEXPRESS'
    database = 'TAPI'
    tabla = 'DiarioTest'

    #SELEC * FROM Diario;

    connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'

    # Conectar a la base de datos
    connection = pyodbc.connect(connection_string)

    # Crear un cursor para ejecutar consultas
    cursor = connection.cursor()

    # TODO: Crear acá la tabla en la BBDD
    #  Consulta SQL
    query = "SELECT TOP 1 FECHA FROM DiarioTest ORDER BY FECHA DESC"

    # Ejecutar la consulta
    df = pd.read_sql(query, connection)

    # Cerrar el cursor
    cursor.close()

    ultimo_dia = df['FECHA'][0].isoformat()
    print(ultimo_dia)
    return ultimo_dia

ultimo_dia_sql()