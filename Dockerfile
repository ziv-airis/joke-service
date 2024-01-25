FROM python:3.9-slim

RUN mkdir /code
COPY . /code
WORKDIR /code/joke-service

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]
