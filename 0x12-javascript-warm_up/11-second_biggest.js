#!/usr/bin/node
const args = process.argv;
if (!process.argv[3]) {
  console.log(0);
} else {
  args.sort();
  let new_args = args.filter((item, index) => args.indexOf(item) === index);
  new_args.shift();
  new_args.shift();
  new_args.reverse();
  console.log(new_args[1]);
}
