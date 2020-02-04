#!/usr/bin/node
const argument = process.argv;
if (argument[3]) {
  console.log('Arguments found');
} else if (argument[2]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
