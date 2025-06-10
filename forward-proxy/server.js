const http = require("http")
const httpProxy = require('http-proxy')
require('dotenv').config()
const proxy = httpProxy.createProxyServer({})
// .env does not support list, so manually turn it into one.

const targets = process.env.TARGETS.split(', ')

const server = http.createServer((req, res) => {
    if (req.url == "/") {
        res.writeHead(200, { 'content-type': 'text/html' });
        res.end('<h1>Hello World!</h1>')
    } else {
        const url = targets[0]
        proxy.web(req, res, { target: url }, (err) => {
            res.writeHead(res.statusCode, { 'content-type': 'text/html' })
            res.end()
        })
    }
})

server.listen(5000, () => {
    console.log(`Proxy server is running on ${process.env.BASE_URL}`)
})
