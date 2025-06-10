const http = require('http')

const httpProxy = require('http-proxy')
require('dotenv').config()
const proxy = httpProxy.createProxyServer({})

const cache = new Map()

// .env does not support list, so manually turn it into one.
// const MINIMUM_NUMBER_OF_WEB_SERVERS = 1
// let index = 0
const target = process.env.TARGET

// function getFreeServer() {
//     const lastIndex = targets.length - 1
//     if (index < lastIndex) {
//         index++;
//         return targets[index]
//     }
//     index = 0;
//     return urls[0]
// }

// function getServer() {
//     if (urls.length > MINIMUM_NUMBER_OF_WEB_SERVERS) {
//         return getFreeServer()
//     }
//     else return urls[0]
// }

const server = http.createServer((req, res) => {
    // let url = getServer()
    // if (url.includes(`"`)) {
    //     url = url.replace(`"`, "")
    // }
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
            proxy.web(req, res, { target: target }, (err) => {
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