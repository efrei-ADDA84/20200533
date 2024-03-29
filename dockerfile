FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir requests==2.31.0

CMD ["python3", "weather.py"]