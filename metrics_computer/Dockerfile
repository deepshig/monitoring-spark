# Use an official Python runtime as a base image
FROM python:3.7

# Without this setting, Python never prints anything out.
ENV PYTHONUNBUFFERED=1

# Set the working directory to the /work directory
WORKDIR /usr/src/app/metrics_computer

# Copy the required contents into the container at /converter
COPY . .

COPY rabbitmq ../rabbitmq

# Install java 8
RUN apt-get update && \
    echo "deb http://ftp.debian.org/debian stretch main" >> /etc/apt/sources.list && \
    echo "deb-src http://ftp.de.debian.org/debian stretch main" >> /etc/apt/sources.list && \
    apt-get update && \
    apt install -y openjdk-8-jdk

# Install the required dependencies (including pyspark)
RUN pip install --no-cache-dir -r ./metrics_computer/requirements.txt

# start command
CMD [ "python", "processor.py" ]
