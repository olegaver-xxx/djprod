FROM python:3.9
COPY src/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY src/ /app/src
WORKDIR /app/src
ENTRYPOINT "/app/src/start_server.sh"