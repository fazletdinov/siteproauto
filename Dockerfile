# pull the official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add gcc python3-dev musl-dev
# install dependencies

RUN pip install --upgrade pip && pip install tzdata
COPY /requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

#EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]