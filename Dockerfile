FROM nginx:latest

#RUN apt install -y python3

RUN apt-get update && \
    apt-get install -y python3 python3-pip

RUN apt install -y python3.11-venv

RUN apt install -y apache2-utils

RUN htpasswd -b -c /etc/nginx/passwords gabo 123456

#RUN openssl req -batch -x509 -nodes -days 365 -newkey rsa:2048 \
#    -keyout /etc/ssl/private/nginx.key \
#    -out /etc/ssl/certs/nginx.crt

#INSTALL FLASK AND COPY REQUIRED DIRECTORIES.
#COPY ./scripts/start_app_servers.py /usr/local/bin/start_app_servers.py
WORKDIR /portforever
COPY . /portforever
COPY ./static /var/www/static
COPY ./templates /var/www/templates

#COPY REQUIRED .CONF FILE.
COPY ./portforever.conf /etc/nginx/conf.d/default.conf
COPY ./index.html /var/www/index.html

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Activate the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Now you can install packages in the virtual environment
RUN pip install --no-cache-dir -r requirements.txt

#COPY REQUIRED CONTENT. 
# Instala las dependencias de tu aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Configura las variables de entorno
ENV FLASK_DEBUG=True
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV SECRET_KEY=esly

#EXECUTE FLASK APP.
#COPY ./scripts/wrapper.sh /docker-entrypoint.d/wrapper.sh          ^T Execute       ^C Location      M-U Undo         M-A Set Mark     M-] To Bracket   M-Q Previous     ^B Back          ^◂ Prev Word     ^A H^
# Ejecuta tu aplicación Flask utilizando el comando "flask run"
CMD ["flask", "run"]
