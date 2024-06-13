#codigo para capturar el último día cargado en la BBDD

import pandas as pd
import pyodbc
from datetime import datetime, timedelta, timezone


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

    ultimo_dia = df['FECHA'][0]

    # # Convertir la cadena a un objeto datetime
    # fecha_dt = datetime.strptime(ultimo_dia, "%Y-%m-%d")

    # # Crear un objeto de zona horaria fija (-03:00)
    # zona_horaria = timezone(timedelta(hours=-3))

    # # Agregar la zona horaria al objeto datetime
    # fecha_dt = fecha_dt.replace(tzinfo=zona_horaria)

    # # Formatear el datetime como una cadena con el método isoformat()
    # fecha_formateada = fecha_dt.isoformat()
    
    return ultimo_dia