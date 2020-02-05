#!/usr/bin/node

const ilegalnumber = isNaN(process.argv[2]);
const decimalnumber = parseInt(process.argv[2]);

if (ilegalnumber) {
  console.log('Not a number');
} else {
  console.log('My number: ' + decimalnumber)
}
