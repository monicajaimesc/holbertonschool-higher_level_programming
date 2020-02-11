#!/usr/bin/node
const fs = require('fs');
const pathTofile = process.argv[2];
const string = process.argv[3];

fs.writeFile(pathTofile, string, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else { console.log(data); }
});
