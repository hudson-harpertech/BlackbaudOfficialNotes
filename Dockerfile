FROM python:3.8-slim-buster

WORKDIR /app

COPY sky-api-python-client-main.zip ./
COPY data ./data
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY main.py .
COPY .sky-token ./

CMD [ "python3", "main.py" ]