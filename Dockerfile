FROM python:3.8

WORKDIR /flask_api
COPY flask_api .
RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install -y nodejs
RUN apt-get install -y ansible
RUN apt-get install -y vim

CMD ["python", "app.py"]