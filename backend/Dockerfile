# pulled official base image
FROM python:3.10.5

# set working directory
WORKDIR /usr/src/support/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# installed dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/support/
RUN pip install -r requirements.txt

# copied project
COPY . /usr/src/support/