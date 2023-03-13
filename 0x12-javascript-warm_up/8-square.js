#!/usr/bin/node
// A script that prints a square
let size = process.argv[2];

if (!Number.isInteger(parseInt(size))) {
   console.log('Missing size');
} else {
  size = parseInt(size);

// Create the square
for (let i = 0; i < size; i++) {
   let row = "";
   for (let j = 0; j < size; j++) {
     row += 'X';
   }
   console.log(row);
   }
}
