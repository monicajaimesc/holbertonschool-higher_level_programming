#!/usr/bin/node

const argument = process.argv[2];
if (argument === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
