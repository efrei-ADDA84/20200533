FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir requests

CMD ["python3", "weather.py"]