#!/usr/bin/node
const Square = require('./5-square');

const r1 = new Square(5, 5);
console.log(r1);
r1.print();
r1.double();
r1.print();
console.log(r1.width);
console.log(r1.height);
