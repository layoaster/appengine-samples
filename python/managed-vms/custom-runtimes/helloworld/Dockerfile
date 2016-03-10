FROM debian:testing

RUN apt-get update && apt-get install -y python2.7 python-pip

RUN pip install WebOb Paste webapp2

ADD . /app
WORKDIR /app

EXPOSE 8080
CMD ["python", "main.py"]