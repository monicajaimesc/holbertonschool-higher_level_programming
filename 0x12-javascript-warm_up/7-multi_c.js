#!/usr/bin/node

const str = 'C is fun';
const x = Number(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let current = 0; current < x; current++) {
    console.log(str);
  }
}
