FROM python:3.10-alpine

WORKDIR /publisher

COPY ./requirements.txt requirements.txt
COPY publisher.py publisher.py

RUN pip install -r requirements.txt

CMD ["python", "-u", "publisher.py"]
