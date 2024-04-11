FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir requests==2.3

CMD ["python3", "weather.py"]