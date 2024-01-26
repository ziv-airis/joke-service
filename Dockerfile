FROM python:3.9-slim

RUN mkdir /code
COPY . /code
WORKDIR /code/joke-service

# Install Git to downlowd the logger packege
RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# TODO maybe add the repo and run locally RUN pip install -e /path/to/your/library
RUN pip install git+https://github.com/ofeks96/ofeklogger.git@main#egg=ofeklogger

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]
