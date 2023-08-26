FROM ubuntu:20.04

# Install necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && \
    apt-get install -y apt-transport-https 
# rm -rf /var/lib/apt/lists/*
RUN apt install curl -y
RUN curl -o Rhubarb-Lip-Sync-1.13.0-Linux.zip -L https://github.com/DanielSWolf/rhubarb-lip-sync/releases/download/v1.13.0/Rhubarb-Lip-Sync-1.13.0-Linux.zip
RUN apt-get install unzip
RUN unzip Rhubarb-Lip-Sync-1.13.0-Linux.zip -d /usr/local/bin
RUN chmod +x /usr/local/bin/Rhubarb-Lip-Sync-1.13.0-Linux/rhubarb

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip3 install --no-cache-dir -r requirements.txt

CMD exec gunicorn --bind :80 --workers 1 --threads 8 --timeout 0 main:app
