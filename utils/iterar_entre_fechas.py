from datetime import datetime, timedelta

def iterar_entre_fechas(fecha_desde, fecha_hasta):
    fecha_actual = datetime.strptime(fecha_desde, "%Y-%m-%dT%H:%M:%S.%f%z")
    fecha_fin = datetime.strptime(fecha_hasta, "%Y-%m-%dT%H:%M:%S.%f%z")

    fecha_actual = fecha_actual.replace(hour=0, minute=0, second=0, microsecond=0)

    while fecha_actual <= fecha_fin:
        fecha_siguiente = fecha_actual + timedelta(hours=23, minutes=59)
        yield fecha_actual, fecha_siguiente
        fecha_actual += timedelta(days=1)