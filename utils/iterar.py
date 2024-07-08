from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def entre_meses(fecha_desde, fecha_hasta):
    fecha_actual = datetime.strptime(fecha_desde, "%Y-%m-%dT%H:%M:%S.%f%z")
    fecha_fin = datetime.strptime(fecha_hasta, "%Y-%m-%dT%H:%M:%S.%f%z")
    
    while fecha_actual < fecha_fin:
        # Primer día del mes actual
        primer_dia_mes = fecha_actual.replace(day=1)
        # Último día del mes actual
        if fecha_actual.month == 12:
            ultimo_dia_mes = fecha_actual.replace(day=31)
        else:
            primer_dia_siguiente_mes = fecha_actual.replace(day=1) + relativedelta(months=1)
            ultimo_dia_mes = primer_dia_siguiente_mes - timedelta(days=1)
        
        yield primer_dia_mes, ultimo_dia_mes
        
        # Avanza al siguiente mes
        fecha_actual = fecha_actual + relativedelta(months=1)

def entre_dias(fecha_desde, fecha_hasta):
    fecha_actual = datetime.strptime(fecha_desde, "%Y-%m-%dT%H:%M:%S.%f%z")
    fecha_fin = datetime.strptime(fecha_hasta, "%Y-%m-%dT%H:%M:%S.%f%z")

    # Asegurarse de que fecha_actual sea exactamente a la medianoche
    fecha_actual = fecha_actual.replace(hour=0, minute=0, second=0, microsecond=0)

    while fecha_actual <= fecha_fin:
        fecha_siguiente = fecha_actual + timedelta(hours=23, minutes=59)
        yield fecha_actual, fecha_siguiente
        # Añadir un día para la próxima iteración
        fecha_actual += timedelta(days=1)
