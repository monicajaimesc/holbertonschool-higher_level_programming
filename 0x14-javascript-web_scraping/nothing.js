#!/usr/bin/node
const request = require('request');
const someServer = process.argv[2]

request.get(someServer, function (error, response, body) {
  if (!error && response.statusCode == 200) {i
    console.log('code:', response.statusCode);
  } else {
    console.log(error);
  }
});


