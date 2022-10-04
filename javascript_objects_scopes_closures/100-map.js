#!/usr/bin/node
const l1 = require('./100-data').list;
const me = [2, 4, 5, 6, 7];
const map1 = me.map((x, y, l1) => x * l1[y]);
console.log(l1);
console.log(map1);
