FROM python:3.9-alpine

ADD ./libs /code

COPY requirements.txt /code/requirements.txt
COPY pubsub_sa.json /code/pubsub_sa.json

WORKDIR /code

RUN pip install -r requirements.txt

# EXPOSE 8089

CMD ["python", "-u", "stream_topics.py"]
