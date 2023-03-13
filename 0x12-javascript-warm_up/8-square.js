#!/usr/bin/node
// A script that prints a square
const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  const square = Array(size).fill('X'.repeat(size));
  console.log(square.join('\n'));
}
