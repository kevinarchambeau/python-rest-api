FROM python:3.12.2-slim-bookworm
RUN mkdir /app
COPY requirements.txt /app
COPY src /app/src
COPY conf /app/conf
COPY demodb.db /app/
RUN pip install -r /app/requirements.txt
CMD gunicorn --bind 0.0.0.0:8080 --chdir /app/src app:app