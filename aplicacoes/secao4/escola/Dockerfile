FROM python:3.10-slim

WORKDIR /code

RUN pip install --no-cache-dir --upgrade pip

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code
