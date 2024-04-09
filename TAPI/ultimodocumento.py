import requests
from datetime import datetime

#Con este script se puede obtener la fecha del último documento cargado por CAMMESA
def  ultimo_dia_CAMM():

    ultimafecha = requests.get("https://api.cammesa.com/pub-svc/public/obtieneFechaUltimoDocumento?nemo=PARTE_POST_OPERATIVO")

    #fecha = str(ultimafecha.text[10:-2])
    fecha = ultimafecha.text[10:-2]
    
    return fecha