#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

const incr = function (x) {
  x = x + 1;
};
myObject.push(incr);

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
