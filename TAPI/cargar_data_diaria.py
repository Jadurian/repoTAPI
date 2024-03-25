import os
import pandas as pd
import zipfile
import pyodbc
import requests
import io
from datetime import datetime, timedelta
import sqlalchemy

#TODO: resta completar

server = 'DARCCVWSQL19'
#server = 'DESKTOP-37ESKFT\SQLEXPRESS'
database = 'TAPI'
tabla = 'DiarioTest'
connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'

excel_path = r"C:\Users\jadurian\OneDrive - Pampa Energia\CDD - Tablero de Análisis de Perdidas de Ingresos\Documentación\2-Fuente de Datos\df_POSOP_diario.xlsx"
name_excel = os.path.basename(excel_path)

#genero dataframe de la ta
df = pd.read_excel(excel_path, sheet_name="Sheet1")
# Renombrar la columna
df.rename(columns={'Fecha_dia': 'FECHA'}, inplace=True)

# Posicionar la nueva columna como la primera columna
nuevas_columnas = ['FECHA'] + [col for col in df if col != 'FECHA']
df = df.reindex(columns=nuevas_columnas)