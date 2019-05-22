# Base Image
FROM ubuntu:18.04
# Layers
RUN apt-get update -y
RUN apt-get install -y python-pip && apt-get install -y python-dev && apt-get install -y build-essential
RUN pip install --user pymysql
# Copy files
COPY . /app
# Change directory
WORKDIR /app
# Default Application
ENTRYPOINT ["python"]
CMD ["db.py"]
