# Imagen base: Usamos una versión oficial de Python
FROM python:3.11-slim-buster
 
# Directorio de trabajo dentro del contenedor
# WORKDIR /app
 
# Copiamos los archivos necesarios (asumiendo que tienes un requirements.txt)
COPY requirements.txt requirements.txt
 
# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && \ apt-get install -y unixodbc unixodbc-dev


# Copiamos el código fuente de tu aplicación
COPY main.py main.py
 
# Puerto en el que tu aplicación estará disponible (ajústalo si es diferente)
EXPOSE 8000
 
# Comando para iniciar tu aplicación (reemplaza 'tu_script.py' con tu archivo principal)
CMD ["python", "main.py"]
