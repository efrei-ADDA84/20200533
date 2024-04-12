FROM python:3.9-alpine

WORKDIR /app

RUN apk add --no-cache build-base=0.5-r3 libffi-dev=3.4.4-r3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV OPENWEATHER_API_KEY=""
ENV FLASK_APP=weather.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8081"]