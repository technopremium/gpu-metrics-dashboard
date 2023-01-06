# pull official base image
FROM python:3.10.5-slim-buster

# set work directory
WORKDIR /usr/src/code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update 
RUN apt-get install gcc python3-dev -y \
    && apt-get clean

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/code/requirements.txt
RUN pip install -r requirements.txt

RUN mkdir entrypoint
# copy entrypoint.sh
COPY ./entrypoint/dev.sh entrypoint/

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["sh", "/usr/src/code/entrypoint/dev.sh"]