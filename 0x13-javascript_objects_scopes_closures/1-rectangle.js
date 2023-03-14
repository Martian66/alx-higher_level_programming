#!/usr/bin/node
// Write a class Rectangle that defines a rectangle
module.exports = class Rectangle {
  constructor (w, h) {
    if (Number.isFinite(w) && Number.isFinite(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
