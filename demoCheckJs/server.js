const http = require('http');
const verify = require('./verify');
var request = require('request');

const hostname = '127.0.0.1';
const port = 5000;

const server = http.createServer((req, res) => {
    if (req.method == 'POST') {
        var body = '';
        req.on('data', function (data) {
            body += data;
            body = JSON.parse(body);
            const isBase64 = verify.isBase64(body.image);
            const isTest = verify.isTest(body.image);
            console.log("\nverify: request from demo proxy", isBase64 ? "is":"is not(!)", "base64 encoded");
            console.log("verify: encoded value from demo proxy", isTest.result ? "is":"is not(!)", "'test'", isTest.result ? "":("it is " + isTest.string));
        });
        res.end("");
    }
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});




// Configure  request
var options = {
    url: "http://127.0.0.1:8081/api/image",
    method: 'POST',
    json:{"image":"test"},
    }

// Send request 
request(options, function (error, response, body) {});


