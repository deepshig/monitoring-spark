# Use an official Python runtime as a base image
FROM python:3.7

# Update apt-get repositories
RUN apt-get update && apt-get install default-jdk --assume-yes

# install pika to access rabbitmq
RUN pip install pika

# Without this setting, Python never prints anything out.
ENV PYTHONUNBUFFERED=1

# Set the working directory to the /work directory
WORKDIR /usr/src/app/metrics_computer

# Copy the required contents into the container at /converter
COPY . .

# Install the required dependencies (including pyspark)
RUN pip install --no-cache-dir -r requirements.txt

# start command
CMD [ "python", "consumer.py" ]
