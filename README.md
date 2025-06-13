# Prototype of full architecture
A small ToDo app, which will serve as a prototype for the next project's architecture.

## Introduction

This is a practice project. In this project there will be a forward proxy (residential), which will "expose" the web server/s to the internet and be the access point of the application. The web server will be a small app which will on its end connect to a reverse proxy. The reverse proxy will act as a connection bridge between the web server/s and the REST API/s. It will also act as a load balancer (the forward proxy will do the same). The REST API will be a simple application which will provide basic CRUD operations. It will connect to a DB - PostgreSQL. That DB will utilize replicas -> Master and 2 slaves. The master will target all the INSERT, UPDATE, DELETE calls, meanwhile the replicas will handle all the SELECT calls, splitting the calls between one another.

### Run the Application

There are three ways of running the application. Two of them are dockerized and the third is a long process:

! Important -> Kill the previous operation if you want to play around with them -> stop all local servers or run `docker compose -f <file> down`
#### Docker - single
Here the app executes with 1 container per service
1) Make sure you are in the root directory.
2) Run the following command: `docker compose -f docker-compose.single.yml up`
3) Additional Info: If you would like you can run the previous command with `-d` at the end. I suggest not to, so that you can see the calls running in the terminal and not have to switch between terminals in the docker envrionment.
#### Docker - multiple
Here the app executes with 1 container for the proxies and 2 containers for the web server and 2 contaienrs for the backend. That way the load balancing can be spectated.
1) Make sure you are in the root directory.
2) Run the following command: `docker compose -f docker-compose.multiple.yml up`
3) Additional Info: If you would like you can run the previous command with `-d` at the end. I suggest not to, so that you can see the calls running in the terminal and not have to switch between terminals in the docker envrionment.
#### Local - long process
The long version requires you to open a few terminals - 1 terminal per service.

Then in no mandatory order tun the following commands:
```javascript 
node server.js // to start the forward-proxy
```

```python 
piepnv run start # for each of the other services 
```

## Architecture

![Current architecture idea for the application](images/arch.drawio.png)

From the architecture we can see that the only endpoint or access point which the client (user utilizng a web browser) will know about is the forward proxy. It will serve as gateway or bridge to the actual web server. The full lines are the presentors or access points. And the dashed lines are the actual elements executing the tasks. We can see that the Forward Proxy connects to the Reverse Proxy, but the actual calls are being done in the web server/s. Similarly to the Forward Proxy it acts as a gateway - acting like it executes the tasks, but in reality it is the REST API. That way the client doesn't know about the web server and Rest API. And the Web Server/Rest API don't know about the client and about each other.

### [Forward Proxy](./forward-proxy/README.md)

The explanation behind the forward proxy you can find in `./forward-proxy/README.md`, or just click on the title.

### [Web Server](./web-server/README.md)

The explanation behind the web server you can find in `./web-server/README.md`, or just click on the title.

### [Reverse Proxy](./reverse-proxy/README.md)

The explanation behind the reverse proxy you can find in `./reverse-proxy/README.md`, or just click on the title.

### [Backend (Including database explanation)](./backend/README.md)

The explanation behind the backend and database you can find in `./backend/README.md`, or just click on the title.
