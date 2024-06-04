from datetime import datetime

# Función para capturar la fecha del nombre del archivo
def fecha_dia(nombre_archivo):
    fecha_str = nombre_archivo[2:4] + "-" + nombre_archivo[4:6] + "-" + nombre_archivo[6:8]
    #print(fecha_str)
    return datetime.strptime(fecha_str, '%y-%m-%d').date()
