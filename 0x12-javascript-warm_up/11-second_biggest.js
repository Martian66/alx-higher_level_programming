#!/usr/bin/node
// A script that searches the second biggest integer in the list of arguments
if (process.argv.length <= 2) {
  console.log('0');
} else if (process.argv.length === 3) {
  console.log('0');
} else {
  const arrNum = process.argv.slice(2).map(Number).filter(Number.isInteger);
  if (arrNum.length <= 1) {
    console.log('0');
  } else {
    const sortedArr = arrNum.sort((a, b) => a - b);
    console.log(sortedArr[sortedArr.length - 2]);
  }
}
