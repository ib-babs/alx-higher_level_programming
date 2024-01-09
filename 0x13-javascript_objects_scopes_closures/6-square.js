#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (!c) c = 'X';
    for (let index = 0; index < this.size; index++) { console.log(c.repeat(this.size)); }
  }
};
