#!/usr/bin/node
// A script that prints the addition of 2 integers
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add (a, b) {
  const x = a + b;
  return x;
}

console.log(add(a, b));
