#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (Number.isFinite(w) && Number.isFinite(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};