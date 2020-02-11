#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const Url = process.argv[2];
const FileName = process.argv[3];

request.get(Url, function (error, response, body) {
  if (!error) {
    // console.log(body);
    fs.writeFile(FileName, body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
