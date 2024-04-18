import os
import pandas as pd
import zipfile
import pyodbc
import requests
import io
from datetime import datetime, timedelta
import sqlalchemy
import urllib
import TAPI

server = 'DARCCVWSQL19'
database = 'TAPI'
tabla = 'DiarioTest'
NEMO = "PARTE_POST_OPERATIVO_UNIF"
URL = f"https://api.cammesa.com/pub-svc/public/"
method_id = "findDocumentosByNemoRango?" 
method_zip = "findAllAttachmentZipByNemoId?"
zip_path = r"C:\Users\Tapi\.zips"
mdb_path = r"C:\Users\Tapi\.zips\.mdb"
connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()
dataframes = []
dfout = pd.DataFrame()
df_filtrado = pd.DataFrame()


#TODO: este script será el main.py que se ejecutará a diario
    # 1_se conectará a la BBDD donde se alojen los históricos
    # 2_capturará la última fecha de carga en la tabla (ultimo_dia_sql.py) la cual será el input FECHA_DESDE
    # 3_se conectará a la API de CAMMESA
    # 4_capturará la última fecha de carga en los documentos de CAMMESA (ultimodocumento.py) la cual será el input FECHA_HASTA
    # 5_procesará la información e insertará los datos en la BBDD 

# 1 Conectar a la BBDD para chequear última fecha subida

fecha_bd = TAPI.ultimo_dia_bd()

a = datetime.fromisoformat(str(fecha_bd))

fecha_desde = a + timedelta(days=1)

fecha_desde = fecha_desde.isoformat()

fecha_hasta = TAPI.ultimo_dia_CAMM()

fecha_hasta = datetime.fromisoformat(str(fecha_hasta))

fecha_hasta = fecha_hasta.isoformat()

print(fecha_desde, type(fecha_desde), fecha_hasta, type(fecha_hasta))