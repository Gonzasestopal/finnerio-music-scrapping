FROM python:3.9

COPY ./src /app/src
COPY requirements.txt /app
COPY scrapy.cfg /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["scrapy"]
