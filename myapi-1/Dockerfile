FROM ubuntu:22.04

# Update the apt package index in non-interactive mode.
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install software-properties-common wget curl -y

# Install python3
RUN apt-get install -y python3 python3-pip

# Install OpenSSL
RUN apt-get install -y openssl libssl-dev

# Install dependencies
ADD requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

# Add files
RUN mkdir -p /opt/app
ADD . /opt/app

# Adjust PYTHONPATH
ENV PYTHONPATH=/opt/app

EXPOSE 8000

WORKDIR /opt/app

CMD uvicorn main:app --host 0.0.0.0 --port 8000 --reload