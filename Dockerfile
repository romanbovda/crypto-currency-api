FROM python:3.9.9-alpine3.14

WORKDIR /app

ENV FLASK_APP="api/app"
ENV FLASK_ENV="development"

COPY requirements.pip requirements.pip

RUN apk add --no-cache curl && pip install -r requirements.pip

COPY . .

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
