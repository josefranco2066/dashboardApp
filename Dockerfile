FROM python:3.6

RUN apt-get update && apt-get install -y apache2 \
    libapache2-mod-wsgi \
    build-essential 

COPY ./app /var/www/apache-flask/app/

COPY requirements.txt /var/www/apache-flask/app/requirements.txt
RUN pip install -r /var/www/apache-flask/app/requirements.txt

COPY ./apache-flask.wsgi /var/www/apache-flask/apache-flask.wsgi
COPY ./apache-flask.conf /etc/apache2/sites-available/apache-flask.conf

COPY ./app /var/www/apache-flask/app/

WORKDIR /var/www/apache-flask
EXPOSE 80
CMD /usr/sbin/apache2ctl -D FOREGROUND