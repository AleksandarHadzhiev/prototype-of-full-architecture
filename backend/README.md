# Backend 

The backend will be build on FastAPI. It will connect to a database, in the case of this prototype it will be a PostgreSQL. The database will have a master and two replicas (slaves).

## Introduction

A simple REST API providing basic CRUD operations. It runs on `PORT=8080` and allows access only from the `reverse-proxy`.

The app is booted up via `uvicorn` and to start it run:

`pipenv run start`

It uses the `pytest` library for testing. To execute the test run:

`pipenv run test`

It connects to a PostgreSQL database in the form of three connections:
- Master DB
- Slave 1 DB - replica
- Slave 2 DB - replica

The master DB handles the `INSERT, DELETE, UPDATE` operations, while the replicas will handle the `SELECT` operations. There is load balancing integration, so that it knows which replica to call to execute the `SELECT` operation. That way it avoids a bottleneck on fetching calls.