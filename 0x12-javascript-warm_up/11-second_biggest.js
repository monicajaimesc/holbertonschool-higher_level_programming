#!/usr/bin/node
const args = process.argv;
if (!process.argv[3]) {
  console.log(0);
} else {
  args.sort(function (a, b) { return a - b });
  const newArgs = args.filter((item, index) => args.indexOf(item) === index);
  newArgs.shift();
  newArgs.shift();
  newArgs.reverse();
  console.log(newArgs[1]);
}
