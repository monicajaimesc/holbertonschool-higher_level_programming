#!/usr/bin/node
const args = process.argv[2];
const x = parseInt(process.argv[2]);
let current = 0;

if (!args || !x) {
  console.log('Missing size');
} else {
  while (current < x) {
    console.log('X'.repeat(x));
    current++;
  }
}
