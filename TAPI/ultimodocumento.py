import requests

#Con este script se puede obtener la fecha del último documento cargado por CAMMESA

ULTIMAFECHA = requests.get("https://api.cammesa.com/pub-svc/public/obtieneFechaUltimoDocumento?nemo=PARTE_POST_OPERATIVO_UNIF")
cadena = str(ULTIMAFECHA)
print(str(ULTIMAFECHA.text[10:-2]))
