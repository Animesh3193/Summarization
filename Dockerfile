FROM python:3.9-alpine

RUN apk update && \
    apk add --virtual build-deps gcc musl-dev gfortran build-base wget freetype-dev libpng-dev openblas-dev

RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "/app/main.py"]