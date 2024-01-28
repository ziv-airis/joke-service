FROM python:3.10-alpine3.16

RUN mkdir /code
COPY . /code
WORKDIR /code/joke-service

# Install Git to download the logger package
RUN apk --no-cache add git sqlite bash

RUN pip install --no-cache-dir -r requirements.txt

# Install the logger package from GitHub -> Added to the requirements but maybe it should stil be mentioned alone
# RUN pip install --upgrade git+https://github.com/ofeks96/ofeklogger.git@main#egg=ofeklogger

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]


# Alpine is smaller (166MB) vs slim (360MB)
# If I want to use slim vs (Deb) Need to change  the following:
# FROM python:3.9-slim 

# Install Git to downlowd the logger packege
# RUN apt-get update && \
#     apt-get install -y git && \
#     apt-get install -y sqlite3 && \
#     rm -rf /var/lib/apt/lists/*
