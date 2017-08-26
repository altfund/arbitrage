FROM python:3.4.3
MAINTAINER gpwclark

# Update phusion and install necessary programs
RUN apt-get update && apt-get install -y \
  git \
  libssl-dev \
  curl \
  ca-certificates \
  wamerican

# Make non sudo user and copy code from git repo to the docker image
RUN useradd -ms /bin/bash user
RUN mkdir -p /home/user/app
ADD . /home/user/app

EXPOSE 5672

# Housekeeping
RUN chown -R user:user /home/user
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /home/user/app
RUN pip install .

USER user
CMD python run_queue.py
