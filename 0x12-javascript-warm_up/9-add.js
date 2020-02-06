#!/usr/bin/node
const args = process.argv;
function add (a, b) {
  return (Number(a) + Number(b));
}
console.log(add(args[2], args[3]));
