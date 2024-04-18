
# for fecha_actual, fecha_siguiente in TAPI.iterar_entre_fechas(fecha_desde, fecha_hasta):
#     valores_generadores = pd.DataFrame()
#     url_doc_id = f"{URL}{method_id}fechadesde={fecha_actual.isoformat()}&fechahasta={fecha_siguiente.isoformat()}&nemo={NEMO}"
    
#     dia_mdb = fecha_actual.strftime("%d-%m-%Y")
#     try:
#         with requests.get(url_doc_id) as response:
#             if response.status_code == 200:
#                 PPO=response.json()
#                 doc_id = PPO[-1]['id']
#                 print(doc_id)
#             else:
#                 print("La solicitud falló con el código de estado:", response.status_code)
#     except requests.exceptions.RequestException as e:
#         print("Error al realizar la solicitud:", e)

#     url_zip = f"{URL}{method_zip}docId={doc_id}&nemo={NEMO}"

#     try:
#         with requests.get(url_doc_id) as response:
#             if response.status_code == 200:
#                 r = requests.get(url_zip)
#                 z = zipfile.ZipFile(io.BytesIO(r.content))
#                 destination_directory = ".zips"
#                 z.extractall(destination_directory)
#                 zip_name = z.namelist()[0]
#             else:
#                 print("La solicitud falló con el código de estado:", response.status_code)

#     except requests.exceptions.RequestException as e:
#         print("Error al realizar la solicitud:", e)
        
#     path_zip_dia = f"{zip_path}\{zip_name}"
  
#     try:
#         with zipfile.ZipFile(path_zip_dia, 'r') as zip_ref:
#             archivo_mdb = os.path.splitext(zip_name)[0] + ".mdb"
#             zip_ref.extract(archivo_mdb, path=mdb_path)

#         mdb_file = os.path.join(mdb_path, archivo_mdb)
#         conn_str = f"Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={mdb_file};"
#         conn = pyodbc.connect(conn_str)
#         valores_generadores = pd.read_sql("SELECT * FROM VALORES_GENERADORES", conn)
#         conn.close()
#         dia_datetime = datetime.strptime(dia_mdb, '%d-%m-%Y')
#         dia_mdb_formatted = dia_datetime.strftime('%Y-%m-%d')
#         valores_generadores.insert(0, 'FECHA', dia_mdb_formatted)
#         quoted = urllib.parse.quote_plus(connection_string)
#         valores_filtrados = ["ADTOHI", "AR21EO", "BAHIEO", "BBLATV29", "BBLATV30",
#                             "BBLMDI01", "BBLMDI02", "BBLMDI03", "BBLMDI04", 
#                             "BBLMDI05", "BBLMDI06", "CERITV01", "CORTEO", 
#                             "EBARTG01", "EBARTG02", "EBARTV01", "ETIGHI", 
#                             "GEBATG01", "GEBATG02", "GEBATG03", "GEBATG04", 
#                             "GEBATV01", "GEBATV02", "GUEMTG01", "GUEMTV11", 
#                             "GUEMTV12", "GUEMTV13", "LDLATG01", "LDLATG02", 
#                             "LDLATG03", "LDLATG04", "LDLATG05", "LDLATV01", 
#                             "LDLMDI01", "LREYHB", "NIH1HI", "NIH2HI", "NIH3HI", 
#                             "PAMEEO", "PEP3EO", "PILBDI01", "PILBDI02", 
#                             "PILBDI03", "PILBDI04", "PILBDI05", "PILBDI06", "PIQIDI01", "PPLEHI"]

#         df_filtrado = valores_generadores[valores_generadores['GRUPO'].isin(valores_filtrados)]   
#         engine = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
#         #df_filtrado.to_sql('DiarioTest', schema='dbo', con=engine, if_exists='append', chunksize=20000)
#         dfout = pd.concat([dfout,df_filtrado], ignore_index=True)

#     except FileNotFoundError:
#         print(f"El archivo {zip_name} no se encontró. Saltando al siguiente archivo...")

# print(dfout)