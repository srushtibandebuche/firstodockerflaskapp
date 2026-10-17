FROM  python:3.12-slim

MAINTAINER softronix<softronix.in>

WORKDIR /app

COPY requirements.txt .

RUN pip install --on-cache-dir -r requirements.txt

COPY . .  

EXPOSE 8000

CMD ["gunicorn","--bind", "0.0.0.0:8000", "app.app"]



