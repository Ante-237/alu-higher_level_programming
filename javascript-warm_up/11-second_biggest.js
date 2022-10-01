#!/usr/bin/node
const args = process.argv;
const conA = Number(args[2]);
let bigSoFar = conA;
if (args.length <= 3) {
  console.log(0);
} else {
  for (let i = 3; i < args.length; i++) {
    if (Number(args[i]) > bigSoFar) {
      bigSoFar = Number(args[i]);
    }
  }
  console.log(bigSoFar);
}
