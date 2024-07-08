#TODO: args: fecha_desde: str, fecha_hassta: str, nemo: str, tabla: str
import os
import pandas as pd
import zipfile
import pyodbc
import requests
import io
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import sqlalchemy
import urllib
import warnings
warnings.filterwarnings('ignore')

from utils.iterar import entre_dias, entre_meses


def dte_corr(fecha_desde: str, fecha_hasta: str):
    NEMO = "DTE_EMISION"

    URL = f"https://api.cammesa.com/pub-svc/public/"

    server = 'DARCCVWSQL19'
    database = 'TAPI'

    tabla_Q_Reporte_Corregidos = 'Q_Reporte_Corregidos'
    tabla_GenTER_Corregidos = 'GenTer_Corregidos'
    tabla_GenHID_Corregidos = 'GenHID_Corregidos'
    tabla_GenMATER_Corregidos = 'GenMATER_Corregidos'
    tabla_GenBOM_Corregidos = 'GenBOM_Corregidos'

    method_id = "findDocumentosByNemoRango?" #ID
    method_zip = "findAllAttachmentZipByNemoId?"

    connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'

    for fecha_actual, fecha_siguiente in entre_meses(fecha_desde,fecha_hasta):
        print("Primer día del mes:", fecha_actual)
        print("Último día del mes:", fecha_siguiente)




def dte_NO_corr(fecha_desde: str, fecha_hasta: str):
    NEMO = "DTE_EMISION"

    URL = f"https://api.cammesa.com/pub-svc/public/"

    server = 'DARCCVWSQL19'
    database = 'TAPI'

    tabla_Q_Reporte_NO_Corregidos = 'Q_Reporte_NO_Corregidos'
    tabla_GenTER_NO_Corregidos = 'GenTer_NO_Corregidos'
    tabla_GenHID_NO_Corregidos = 'GenHID_NO_Corregidos'
    tabla_GenMATER_NO_Corregidos = 'GenMATER_NO_Corregidos'
    tabla_GenBOM_NO_Corregidos = 'GenBOM_NO_Corregidos'

    method_id = "findDocumentosByNemoRango?" #ID
    method_zip = "findAllAttachmentZipByNemoId?"

    connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'    