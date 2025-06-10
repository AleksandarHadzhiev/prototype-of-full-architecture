const http = require('http')

const httpProxy = require('http-proxy')
require('dotenv').config()
const proxy = httpProxy.createProxyServer({})

const cache = new Map()

let index = 0
const target = process.env.TARGET
function getFreeServer(targets) {
    const lastIndex = targets.length - 1
    if (index < lastIndex) {
        index++;
        return targets[index]
    }
    index = 0;
    return targets[0]
}

function getServer() {
    // .env does not support list, so manually turn it into one.
    if (target.includes(", ")) {
        const targets = target.split(", ")
        return getFreeServer(targets)
    }
    else return target
}

const server = http.createServer((req, res) => {
    let url = getServer()
    if (req.url == "/") {
        res.writeHead(200, { 'content-type': 'text/html' })
        res.end(`<h1>We are runnig on port:${process.env.PORT} and the web server is on: ${target}</h1>`)
    }
    else {
        if (cache.has(req.url)) {
            res.writeHead(200, { 'content-type': 'text/html' })
            res.end(cache.get(req.url))
        }
        else {
            proxy.web(req, res, { target: url }, (err) => {
                res.writeHead(res.statusCode, { 'content-type': 'text/html' })
                res.end()
            })
            const socket = res.socket;
            socket.origWrite = socket.write;
            socket.write = function (data, encoding, callback) {
                if (Buffer.isBuffer(data)) {
                    cache.set(req.url, data.toString())
                }
                else {
                    cache.set(req.url, data.toString())
                }
                return socket.origWrite(data, encoding, callback);
            }
        }
    }
})

server.listen(process.env.PORT, () => {
    console.log(`Proxy server is running on ${process.env.BASE_URL}`)
})