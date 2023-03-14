#!/usr/bin/node
// Write a class Rectangle that defines a rectangle
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || w === undefined || h <= 0 || h === undefined) {
      return;
     }
      this.width = w;
      this.height = h;
   }

   print (c) {
     c = 'X';
     for (let i = 0; i < this.height; i++) {
	console.log(c.repear(this.width));
     }
   }
};
