#!/usr/bin/node
// A  script that prints x times “C is fun”

const arg = process.argv[2];
const x = parseInt(arg);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let count = 0;
  while (count < x) {
     console.log('C is fun');
     count++;
   }
}
