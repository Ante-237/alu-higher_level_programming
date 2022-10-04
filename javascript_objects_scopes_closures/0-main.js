#!/usr/bin/node
const Rectangle = require('./4-rectangle');

const r1 = new Rectangle(5, 5);
console.log(r1);
r1.print();
r1.double();
r1.print();
console.log(r1.width);
console.log(r1.height);
