#!/usr/bin/node
// A script that prints the addition of 2 integers

function add(a, b) {
  console.log(a + b);
}
const args = process.argv.slice(2);
const a = parseInt(args[0]);
const b = parseInt(args[1]);

add(a, b);
