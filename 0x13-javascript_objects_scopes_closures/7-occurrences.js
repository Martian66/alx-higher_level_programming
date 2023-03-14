#!/usr/bin/node
// A function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
 let i = 0;
  list.forEach(count);
  function count (obj) {
    if (obj === searchElement) {
      i++;
    }
  }
  return i;
};
