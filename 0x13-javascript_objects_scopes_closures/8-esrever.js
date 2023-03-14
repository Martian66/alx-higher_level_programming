#!/usr/bin/node
// Write a function that returns the reversed version of a list
exports.esrever = function (list) {
  let reversedList = [];
  while (list.length) {
    reversedList.push(list.pop());
  }
  return reversedList;
};
