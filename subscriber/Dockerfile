FROM python:3.10-alpine

WORKDIR /subscriber

COPY ./requirements.txt requirements.txt
COPY subscriber.py subscriber.py

RUN pip install -r requirements.txt

CMD ["python", "-u", "subscriber.py"]