FROM python:3.10-slim-buster

WORKDIR /app

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
COPY app/. .
CMD uvicorn server:app --host 0.0.0.0 --port $PORT