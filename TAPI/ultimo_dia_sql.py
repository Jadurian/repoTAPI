#codigo para capturar el último día cargado en la BBDD

import pandas as pd
import pyodbc
from datetime import datetime, timedelta


def ultimo_dia_bd():
    server = 'DARCCVWSQL19'
    #server = 'DESKTOP-37ESKFT\SQLEXPRESS'
    database = 'TAPI'
    tabla = 'DiarioTest'

    connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'

    # Conectar a la base de datos
    connection = pyodbc.connect(connection_string)

    # Crear un cursor para ejecutar consultas
    cursor = connection.cursor()

    # TODO: Crear acá la tabla en la BBDD
    #  Consulta SQL
    query = f"SELECT TOP 1 FECHA FROM {tabla} ORDER BY FECHA DESC"

    # Ejecutar la consulta
    df = pd.read_sql(query, connection)

    # Cerrar el cursor
    cursor.close()

    ultimo_dia = df['FECHA'][0].isoformat()
    
    #ultimo_dia_siguiente = ultimo_dia.fromisoformat(ultimo_dia) + timedelta(days=1)

    return ultimo_dia


