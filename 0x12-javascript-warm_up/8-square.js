#!/usr/bin/node

const x = Number(process.argv[2]);
let current = 0;

if (isNaN(x) || process.argv[2] === undefined ) {
  console.log('Missing number of occurrences');
} else {
  while (current < x) {
    console.log('X'.repeat(x));
    current++;
  }
}
