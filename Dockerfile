FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ /app/app
COPY app.py /app

CMD ["python", "app.py"]
