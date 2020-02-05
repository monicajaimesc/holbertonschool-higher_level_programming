#!/usr/bin/node
let args = process.argv[2];
const x = Number(process.argv[2]);
let current = 0;

if (!args || !parseInt(args)) {
  console.log('Missing number of occurrences');
} else {
  while (current < x) {
    console.log('X'.repeat(x));
    current++;
  }
}
