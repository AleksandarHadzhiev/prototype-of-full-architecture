# Reverse Proxy

This proxy, will be the endpoint which the web server will access, instead of the backend itself. The proxy will redirect the calls to the backend, adding an additional layer of security, by hiding the real endpoint of the backend server. It will also provide cache, and a load balancer.

## Introduction

This is the bridge between web server and backend. It is running on FastAPI server, started by `uvicorn`. To run it simply run: `pipenv run start`. If the backend is not running it doesn't do anything, as it is static in the connections it allows - receive from the forward-proxy (the calls are actually made by the web server) and forward to the backend and vice versa.

To forward the requests it is using the `requests` library (calls the backend). To run and build tests it uses the `pytest` library.

To execute the tests run: `pipenv run test`

Not only it acts as a bridge by redirecting the calls, but also as a load balancer. Similarly to the forward proxy it uses the round robin strategy for choosing which server to redirect the call to.

The app runs on `PORT=8000`.