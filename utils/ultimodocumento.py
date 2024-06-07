import requests
from datetime import datetime, timedelta, timezone

#Con este script se puede obtener la fecha del último documento cargado por CAMMESA
def  ultimo_dia_CAMM():

    ultimafecha = requests.get("https://api.cammesa.com/pub-svc/public/obtieneFechaUltimoDocumento?nemo=PARTE_POST_OPERATIVO")

    #fecha = str(ultimafecha.text[10:-2])
    
    fecha = ultimafecha.text[10:-2]

    # # Convertir la cadena a un objeto datetime
    # fecha_dt = datetime.strptime(fecha, "%Y-%m-%d")

    # # Crear un objeto de zona horaria fija (-03:00)
    # zona_horaria = timezone(timedelta(hours=-3))

    # # Agregar la zona horaria al objeto datetime
    # fecha_dt = fecha_dt.replace(tzinfo=zona_horaria)

    # # Formatear el datetime como una cadena con el método isoformat()
    # fecha_formateada = fecha_dt.isoformat()

    return fecha