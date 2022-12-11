FROM python:3.9

COPY ./src /app/src
COPY requirements.txt /app
COPY app.py /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python", "app.py"]
