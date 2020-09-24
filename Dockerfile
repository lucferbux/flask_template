FROM python:3.8.5-buster

LABEL maintainer="lucasfernandezaragon@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app

# Update working directory
WORKDIR /usr/src/app

# copy everything from this directory to server/flask docker container
COPY . /usr/src/app/

# Give execute permission to below file, so that the script can be executed by docker.
RUN chmod 777 /usr/src/app/entrypoint.sh

# Install the Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# run server
CMD ["./entrypoint.sh"]