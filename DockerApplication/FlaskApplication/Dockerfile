# Dockerization of simple Flask Application in Ubuntu Linux machine
# Base Image
FROM ubuntu:latest
# Layers
RUN apt-get update -y
RUN apt-get install -y python-pip && apt-get install -y python-dev
RUN apt-get install -y build-essential && pip install --user flask
# Copy from host to the image 
COPY . /app
# Change Directory
WORKDIR /app
# Runtime Environment
ENTRYPOINT ["python"]
# Commands to execute
CMD ["scott.py"]
