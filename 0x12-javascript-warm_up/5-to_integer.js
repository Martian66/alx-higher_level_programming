#!/usr/bin/node
// A script that prints My number: <first argument converted in integer>
const num = parseInt(process.argv[2]);

if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
