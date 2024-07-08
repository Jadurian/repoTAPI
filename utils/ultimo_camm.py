import requests
from datetime import datetime, timedelta, timezone

#Con este script se puede obtener la fecha del último documento cargado por CAMMESA
def  ultimo_dia_came(nemo:str) -> str:

    url = requests.get(f"https://api.cammesa.com/pub-svc/public/obtieneFechaUltimoDocumento?nemo={nemo}")
    fecha = url.text[10:-2]

    return fecha