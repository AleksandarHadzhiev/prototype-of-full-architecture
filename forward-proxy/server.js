const http = require("http")
const httpProxy = require('http-proxy')
require('dotenv').config()
console.log(process.env.ENV)
const proxy = httpProxy.createProxyServer({})

const targets = process.env.TARGETS

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
