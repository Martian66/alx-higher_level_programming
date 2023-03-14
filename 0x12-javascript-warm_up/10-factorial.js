#!/usr/bin/node
// A script that computes and prints a factorial
const n = parseInt(process.argv[2]);

function factorial (n) {
  if (Number.isNaN(n) || n === 0) {
    return (1);
  }
  if (n < 0) {
    return (-1);
  }
  return (n * factorial(n - 1));
}

console.log(factorial(n));
