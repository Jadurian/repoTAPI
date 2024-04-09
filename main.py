import TAPI
from datetime import datetime, date, timedelta

#TODO: este script será el main.py que se ejecutará a diario
    # 1_se conectará a la BBDD donde se alojen los históricos
    # 2_capturará la última fecha de carga en la tabla (ultimo_dia_sql.py) la cual será el input FECHA_DESDE
    # 3_se conectará a la API de CAMMESA
    # 4_capturará la última fecha de carga en los documentos de CAMMESA (ultimodocumento.py) la cual será el input FECHA_HASTA
    # 5_procesará la información e insertará los datos en la BBDD 

# 1 Conectar a la BBDD para chequear última fecha subida

#from TAPI import ultimo_dia_sql

fecha_bd = TAPI.ultimo_dia_bd()

a = datetime.fromisoformat(fecha_bd)

fecha_desde = a + timedelta(days=1)

fecha_desde = fecha_desde.isoformat()

fecha_hasta = TAPI.ultimo_dia_CAMM()

print(fecha_hasta)

