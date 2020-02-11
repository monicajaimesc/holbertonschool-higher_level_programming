#!/usr/bin/node
const request = require('request');
const parameter = process.argv[2];
const requestURL = 'http://swapi.co/api/films/';
// 0 is '/usr/bin/node'
// console.log(process.argv)
request(requestURL + parameter, function (error, response, body) {
  if (!error) {
    console.log(JSON.parse(body).title);
  }
});
