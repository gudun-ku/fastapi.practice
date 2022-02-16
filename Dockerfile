FROM python:3.10-slim-buster

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH=”$VIRTUAL_ENV/bin:$PATH”

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./start.sh /start.sh
RUN chmod +x /start.sh


# Run the application:
COPY server.py .
CMD ["./start.sh"]