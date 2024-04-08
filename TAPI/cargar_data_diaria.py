import os
import pandas as pd
import zipfile
import pyodbc
import requests
import io
from datetime import datetime, timedelta
import sqlalchemy

from TAPI.ultimo_dia_sql import ultimo_dia_sql

#TODO: este script será el main.py que se ejecutará a diario
    # 1_se conectará a la BBDD donde se alojen los históricos
    # 2_capturará la última fecha de carga en la tabla (ultimo_dia_sql.py) la cual será el input FECHA_DESDE
    # 3_se conectará a la API de CAMMESA
    # 4_capturará la última fecha de carga en los documentos de CAMMESA (ultimodocumento.py) la cual será el input FECHA_HASTA
    # 5_procesará la información e insertará los datos en la BBDD 


server = 'DARCCVWSQL19'
#server = 'DESKTOP-37ESKFT\SQLEXPRESS'
database = 'TAPI'
tabla = 'DiarioTest'
connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'

excel_path = r"C:\Users\jadurian\OneDrive - Pampa Energia\CDD - Tablero de Análisis de Perdidas de Ingresos\Documentación\2-Fuente de Datos\df_POSOP_diario.xlsx"
name_excel = os.path.basename(excel_path)

# 1 Conectar a la BBDD para chequear última fecha subida

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

fecha_hasta = ultimo_dia_sql()

print(fecha_hasta)