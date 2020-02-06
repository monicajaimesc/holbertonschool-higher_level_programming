#!/usr/bin/node
const digit = parseInt(process.argv[2]);

function factorial (number) {
  if (!number) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}
console.log(factorial(digit));
