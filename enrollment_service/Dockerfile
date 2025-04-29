FROM python:3.12-slim

WORKDIR /app

COPY app.py .

RUN pip install --no-cache-dir Flask requests

EXPOSE 5003

CMD ["python", "app.py"]
