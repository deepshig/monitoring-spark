# Use an official Python runtime as a base image
FROM python:3.7

# Update apt-get repositories
RUN apt-get update && apt-get install default-jdk --assume-yes

# Set the working directory to the /work directory
WORKDIR /work

# Copy the required contents into the container at /converter
ADD ./read_data.py          /work/read_data.py
ADD ./query.py              /work/query.py
ADD ./sample_data.csv       /work/sample_data.csv
ADD ./requirements.txt      /work/requirements.txt

# Install the required dependencies (including pyspark)
RUN pip install --no-cache-dir -r requirements.txt

