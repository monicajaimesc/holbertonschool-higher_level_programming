#!/usr/bin/node
const a = 'Arguments found'
const c = 'Arguments found'
const b = 'No argument'

if (process.argv[3]) {
  console.log(a)
} else if (process.argv[2]) {
  console.log(c)
} else {
  console.log(b)
}
