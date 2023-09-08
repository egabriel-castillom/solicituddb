# Utiliza una imagen de Python 3.11 como base
FROM python:3.11.3

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de tu aplicación Flask en el contenedor
COPY . /app

# Instala las dependencias de tu aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Configura las variables de entorno
ENV FLASK_DEBUG=True
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV SECRET_KEY=esly

# Ejecuta tu aplicación Flask utilizando el comando "flask run"
CMD ["flask", "run"]
