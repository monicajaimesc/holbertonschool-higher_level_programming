#!/usr/bin/node
const args = process.argv;
if (!process.argv[3]) {
  console.log(0);
} else {
  console.log(args.sort().reverse()[1]);
}
