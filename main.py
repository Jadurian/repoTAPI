#libs

import os
import pandas as pd
import zipfile
import pyodbc
import requests
import io
from datetime import datetime, timedelta
import sqlalchemy
import urllib

#funciones

def iterar_entre_fechas(fecha_desde, fecha_hasta): #iteracion entre fechas
    fecha_actual = datetime.strptime(fecha_desde, "%Y-%m-%dT%H:%M:%S.%f%z")
    fecha_fin = datetime.strptime(fecha_hasta, "%Y-%m-%dT%H:%M:%S.%f%z")

    # Asegurarse de que fecha_actual sea exactamente a la medianoche
    fecha_actual = fecha_actual.replace(hour=0, minute=0, second=0, microsecond=0)

    while fecha_actual <= fecha_fin:
        fecha_siguiente = fecha_actual + timedelta(hours=23, minutes=59)
        yield fecha_actual, fecha_siguiente
        # Añadir un día para la próxima iteración
        fecha_actual += timedelta(days=1)
        
def  ultimo_dia_CAMM(): #Con este script se puede obtener la fecha del último documento cargado por CAMMESA

    ultimafecha = requests.get("https://api.cammesa.com/pub-svc/public/obtieneFechaUltimoDocumento?nemo=PARTE_POST_OPERATIVO")
    
    fecha = ultimafecha.text[10:-2]

    return fecha

def ultimo_dia_bd(): #captura la fecha del último registro cargado en la BD
    server = 'DARCCVWSQL19'
    database = 'TAPI'
    tabla = 'Valores_Gen_Diario_Automatico'

    connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'

    connection = pyodbc.connect(connection_string)

    cursor = connection.cursor()

    query = f"SELECT TOP 1 FECHA FROM {tabla} ORDER BY FECHA DESC"

    df = pd.read_sql(query, connection)

    cursor.close()

    ultimo_dia = df['FECHA'][0]

    return ultimo_dia

# Ejecucion de codigo

server = 'DARCCVWSQL19'
database = 'TAPI'

tabla_valores = 'Valores_Gen_Diario_Automatico'
tabla_contratos = 'Contratos_Diario_Automatico'

# Fechas para seleccionar el día de la carga se debe iterar

fecha_desde_obj = datetime.fromisoformat(ultimo_dia_bd())

fecha_hasta_obj = datetime.fromisoformat(ultimo_dia_CAMM())

fecha_desde_bd = ultimo_dia_bd() #OJO DE QUE TABLA TOMA EL ULTIMO DIA

fecha_datetime = datetime.strptime(fecha_desde_bd, "%Y-%m-%d")

fecha_siguiente = fecha_datetime + timedelta(days=1) #Sumar un día

fecha_desde = fecha_siguiente.strftime("%Y-%m-%d") #Convertir de nuevo a string si es necesario

fecha_hasta = ultimo_dia_CAMM() #ultimo informe en API CAMMESA

fecha_desde = fecha_desde+"T00:00:00.000-03:00" 
fecha_hasta = fecha_hasta+"T23:59:00.000-03:00"


NEMO = "PARTE_POST_OPERATIVO"

URL = f"https://api.cammesa.com/pub-svc/public/"

method_id = "findDocumentosByNemoRango?" #ID
method_zip = "findAllAttachmentZipByNemoId?"


zip_path = r"C:\Users\jadurian\Documents\Tapi\.zips"
mdb_path = r"C:\Users\jadurian\Documents\Tapi\.zips\.mdb"

connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'

conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

dataframes = []
dfout = pd.DataFrame()
dfout2 = pd.DataFrame()
df_filtrado = pd.DataFrame()

if fecha_desde_obj < fecha_hasta_obj:
    print("Se realiza el update")

    for fecha_actual, fecha_siguiente in iterar_entre_fechas(fecha_desde, fecha_hasta):

        valores_generadores = pd.DataFrame()
        contrato_abastecimiento = pd.DataFrame()

        url_doc_id = f"{URL}{method_id}fechadesde={fecha_actual.isoformat()}&fechahasta={fecha_siguiente.isoformat()}&nemo={NEMO}"
        
        #obtener el doc_id del dia actual (corregido)
        dia_mdb = fecha_actual.strftime("%d-%m-%Y")
        try:
            with requests.get(url_doc_id) as response:
                if response.status_code == 200:
                    PPO=response.json()
                    doc_id = PPO[-1]['id']
                    print(dia_mdb)
                else:
                    print("La solicitud falló con el código de estado:", response.status_code)
        except requests.exceptions.RequestException as e:
            # Manejar la excepción
            print("Error al realizar la solicitud:", e)

        url_zip = f"{URL}{method_zip}docId={doc_id}&nemo={NEMO}"

        #descargar el .zip del doc_id (corregido)

        try:
            with requests.get(url_doc_id) as response:
                if response.status_code == 200:
                    r = requests.get(url_zip)

                    # Crear un objeto ZipFile a partir del contenido descargado
                    z = zipfile.ZipFile(io.BytesIO(r.content))

                    # Directorio de destino para extraer los archivos ZIP
                    destination_directory = ".zips"

                    # Extraer todos los archivos del ZIP en el directorio específico
                    z.extractall(destination_directory)
                    zip_name = z.namelist()[0]
                else:
                    print("La solicitud falló con el código de estado:", response.status_code)

        except requests.exceptions.RequestException as e:
            # Manejar la excepción
            print("Error al realizar la solicitud:", e)
        
        #Colocar los PATHs correctos donde se traeran los archivos
        
        path_zip_dia = f"{zip_path}\{zip_name}"

        #display(path_zip_dia)

        
        try:
            # Extrae el archivo MDB de cada archivo ZIP diario
            with zipfile.ZipFile(path_zip_dia, 'r') as zip_ref:
                # Encontrar el nombre del archivo MDB dentro del ZIP diario
                archivo_mdb = os.path.splitext(zip_name)[0] + ".mdb"
                zip_ref.extract(archivo_mdb, path=mdb_path)

    
            # Lee el archivo MDB y cargar la tabla VALORES_GENERADORES en un dataframe
            mdb_file = os.path.join(mdb_path, archivo_mdb)
            conn_str = f"Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={mdb_file};"
            conn = pyodbc.connect(conn_str)

            #3
            #-------------------------------------------------------#
            valores_generadores = pd.read_sql("SELECT * FROM VALORES_GENERADORES", conn)
            contrato_abastecimiento = pd.read_sql("SELECT * FROM CONTRATO_ABASTECIMIENTO", conn)
            #-------------------------------------------------------#
            conn.close()
            
            # Convertir dia_mdb a un objeto datetime
            dia_datetime = datetime.strptime(dia_mdb, '%d-%m-%Y')

            # Formatear la fecha en el formato YYYY-MM-DD como una cadena
            dia_mdb_formatted = dia_datetime.strftime('%Y-%m-%d')

            # Insertar la fecha formateada en la lista valores_generadores
            
            #4
            #-------------------------------------------------------#
            valores_generadores.insert(0, 'FECHA', dia_mdb_formatted)

            contrato_abastecimiento.insert(0, 'FECHA', dia_mdb_formatted)
            #-------------------------------------------------------#
            quoted = urllib.parse.quote_plus(connection_string)

            #Por limitaciones de tamaño de excel filtramos solo las máquinas Pampa
            valores_filtrados = ["ADTOHI", "AR21EO", "BAHIEO", "BBLATV29", "BBLATV30",
                                "BBLMDI01", "BBLMDI02", "BBLMDI03", "BBLMDI04", 
                                "BBLMDI05", "BBLMDI06", "CERITV01", "CORTEO", 
                                "EBARTG01", "EBARTG02", "EBARTV01", "ETIGHI", 
                                "GEBATG01", "GEBATG02", "GEBATG03", "GEBATG04", 
                                "GEBATV01", "GEBATV02", "GUEMTG01", "GUEMTV11", 
                                "GUEMTV12", "GUEMTV13", "LDLATG01", "LDLATG02", 
                                "LDLATG03", "LDLATG04", "LDLATG05", "LDLATV01", 
                                "LDLMDI01", "LREYHB", "NIH1HI", "NIH2HI", "NIH3HI", 
                                "PAMEEO", "PEP3EO", "PILBDI01", "PILBDI02", 
                                "PILBDI03", "PILBDI04", "PILBDI05", "PILBDI06", "PIQIDI01", "PPLEHI"]
            
            contratos_filtrados = ["C.T. LOMA DE LA LATA", "C.T.E.BARRAGAN TV-M", "CT LOMA II LA LATA-M", "GENELBA CC -MERCA", "PIEDRABUENA  R21-","CT PILAR BS AS M"]

            df_valores = valores_generadores[valores_generadores["GRUPO"].isin(valores_filtrados)]  
            
            df_contratos = contrato_abastecimiento[contrato_abastecimiento["CONTRATO"].isin(contratos_filtrados)] 

            engine = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
        
            df_valores.to_sql(f'{tabla_valores}', schema='dbo', con=engine, if_exists='append', chunksize=20000)

            df_contratos.to_sql(f'{tabla_contratos}', schema='dbo', con=engine, if_exists='append', chunksize=20000)
            
        except FileNotFoundError:
            print(f"El archivo {zip_name} no se encontró. Saltando al siguiente archivo...")
else:
    print(f"Última fecha en BD:{fecha_desde_obj} es igual a la última fecha del informe de CAMMESA: {fecha_hasta_obj}\nNo se realiza el update")

print("Finaliza el update")