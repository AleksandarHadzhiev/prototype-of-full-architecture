# Web Server

The web server will be built on fastapi, which will start an http server. The http server will give access to the content of the web app: HTML, CSS, JavaScript.

## Introduction

There are two sides to the web server. A FastAPI server which boots up the application and provides endpoints. And a client side so to say - `HTML, CSS, JS` files. With the `JS` files executing the FastAPI endpoints.

### FastAPI

It is a very simple app running on `PORT=3000`. It allows only the `forward-proxy` to access it. And it sends requests to the `reverse-proxy` via the `requests` library. The server is started via the `uvicorn` library. To run and build tests the `pytest` library is utilized.

To run the tests simply run: `pipenv run test`.

To boot up the application simply run: `pipenv run start`.

The client side is connected to the server side via the `HTML` files which can be found in the `templates` dir. The client side makes calls via `fetch` and it is using the relative paths -> `/path` provided by the server.