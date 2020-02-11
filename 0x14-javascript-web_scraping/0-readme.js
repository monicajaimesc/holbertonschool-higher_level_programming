#!/usr/bin/node
// importing the fs package
const fs = require('fs');
const pathTofile = process.argv[2];

fs.readFile(pathTofile, 'utf8', function (err, data) {
  // result in one ENOENT 2 No such file or directory
  if (err) {
    console.log(err);
  } else { console.log(data); }
});
