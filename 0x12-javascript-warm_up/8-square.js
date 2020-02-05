#!/usr/bin/node
const args = process.argv[2];
const x = parseInt(process.argv[2]);
let current = 0;

if (parseInt(args)) {
  console.log('Missing number of occurrences');
} else {
  while (current < x) {
    console.log('X'.repeat(x));
    current++;
  }
}
