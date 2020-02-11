#!/usr/bin/node

const request = require('request');
const server = process.argv[2];
request.get(server, function (error, response) {
  if (!error) {
    console.log('code: ' + response.statusCode);
  } else {
    console.log(error);
  }
});
