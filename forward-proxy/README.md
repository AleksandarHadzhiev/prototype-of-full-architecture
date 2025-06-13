## Forward Proxy

This proxy, will be the endpoint which the browser (end-user) will access, instead of the web server itself. The proxy will redirect the calls to the web-server, adding an additional layer of security, by hiding the real endpoint of the web server. It will also provide cache, and a load balancer.

## Introduction

The forward proxy will serve as a bridge between the outside (the internet) and the inside (the application). It will run on an http server in node.js. The `PORT` on which it is running is `5000`. It's main functionality is to forward the call from the internet to the web server. To do that the `http-proxy` library is used. Which simplieifes the forwarding. Additionally the `dotenv` library is utilized for easier access to the `.env` variables. If you want to run it separately from the other services, go to the `forward-proxy` dir and simple run:

```node server.js```

If booted up correctly you will see the following message:

```Proxy server is running on http://127.0.0.1:5000```

You will not be able to do anything on it, since the web-server is not booted up. It is static (residential) in its implementation. It only redirects and serves as a gateway to the web-server.

Some of its other functionalities are load balancer. As you can see in the function `getServer` on line `21`. It turns a `string` of targets into a `list` of targets. That way it knows whether it is serving one or multiple web-servers. And in the `getFreeServer` function on line `11` you can see that it is using the round robin strategy to swich between which web server to redirect to.

Additionally it is providing very basic caching. It is done in a very simple form: 

```const cache = new Map()```

The cache is simple `Map` variable which as key stores the endpoint and as value stores the response - which is some form of `HTML`. That way a call to the same static endpoint is not done again.