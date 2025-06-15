FROM python:3.12-slim

WORKDIR /

COPY Pipfile Pipfile.lock ./

RUN apt-get update && \
    apt-get install -y libpq-dev gcc
RUN pip install pipenv
RUN pipenv --version
RUN pipenv install 

COPY  . .

EXPOSE 8080

CMD ["pipenv", "run", "docker"]