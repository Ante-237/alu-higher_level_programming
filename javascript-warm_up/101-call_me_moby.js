#!/usr/bin/node
export * from '101-call_me_moby.js';
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}
