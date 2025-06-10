const http = require("http")
require('dotenv').config()
console.log(process.env.ENV)

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'content-type': 'text/html' });
    res.end('<h1>Hello World!</h1>')
})


server.listen(5000, () => {
    console.log(`Proxy server is running on ${process.env.BASE_URL}`)
})
