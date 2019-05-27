FROM python:3

RUN apt-get update

COPY  ./requirements.txt /requirements.txt
RUN pip3 install -r  /requirements.txt

COPY /flask_app/. /flask_app/ 

WORKDIR /flask_app

ENV FLASK_APP=docker_logs.py

EXPOSE 5000 

CMD ["flask", "run", "--host=0.0.0.0"]
