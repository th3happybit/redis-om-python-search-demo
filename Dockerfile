FROM python:3.9-alpine

ENV APP_PATH /opt/redis-om-search

RUN apk update && apk add --virtual build-deps gcc python3-dev libffi-dev musl-dev

#installing django
COPY requirements.txt /
RUN pip install -r requirements.txt
RUN rm requirements.txt

ENTRYPOINT ["python", "-m", "http.server", "80"]

RUN mkdir -p $APP_PATH
COPY . $APP_PATH