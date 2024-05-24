FROM python:3.12-slim as p
ENV PYTHONUNBUFFERED 1

COPY .web /app
COPY requirements.txt /app

WORKDIR /app
COPY . .

RUN "pip install -r requirements.txt"
CMD [ "reflex", "run", "--loglevel debug" ]

EXPOSE 3000