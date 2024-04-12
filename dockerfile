FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./

ENV OPENWEATHER_API_KEY=""
ENV FLASK_APP=weather.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8081"]