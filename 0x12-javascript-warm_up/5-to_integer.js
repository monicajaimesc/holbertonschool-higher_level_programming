#!/usr/bin/node

const ilegal_number = isNaN(process.argv[2]);
let decimal_number = parseInt(process.argv[2]);

if (ilegal_number) {
  console.log('Not a number');
} else {
  console.log('My number: ' + decimal_number)
}
