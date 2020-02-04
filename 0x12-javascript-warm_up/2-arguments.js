#!/usr/bin/node
let a = 'Arguments found';
let b = 'No argument';

if (process.argv[3]){
    console.log(a);
} else if (process.argv[2]) {
    console.log(a);
} else {
    console.log(b);
}
