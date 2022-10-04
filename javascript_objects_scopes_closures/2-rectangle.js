#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
    if (this.width <= 0 || this.height <= 0 || (!this.width) || (!this.height)) {
      this.output = {};
      return this.output;
    }
  }
};
