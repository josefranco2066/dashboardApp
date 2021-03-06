FROM python:3.6

EXPOSE 8050

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY ./app /app/

CMD python index.py