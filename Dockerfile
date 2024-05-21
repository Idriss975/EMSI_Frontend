FROM python:3.12

COPY .web /app
WORKDIR /app
COPY . .

RUN "./bin/pip install -r requirements.txt"
CMD [ "./bin/python", "reflex", "run", "--loglevel debug" ]

EXPOSE 3000