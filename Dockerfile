# Template base de dockerfile, modificar como sea necesario
FROM amazonlinux:latest

# Actualizar sistema e instalar dependencias de python
RUN yum update -y && \
    yum install -y python3 python3-pip gcc-c++ 

# Instalar librerías necesarias de python
RUN pip3 install flask

WORKDIR /app

# Copiar código de aplicación al workdir
COPY . /app

# Exponer puerto para el servidor
EXPOSE 8080

# Configuracion de variables de entorno de flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Ejecuta la aplicación de flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
