FROM python:3.10-slim-buster

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH=”$VIRTUAL_ENV/bin:$PATH”

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
COPY server.py .
#CMD ["uvicorn","server:app","--host", "0.0.0.0","--port","${PORT:8000}"]
CMD uvicorn server:app --host 0.0.0.0 --port $PORT