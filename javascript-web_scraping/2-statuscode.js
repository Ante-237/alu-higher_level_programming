#!/usr/bin/node
const args = process.argv;
const request = require('request');

request.get(args[2], function (response) {
  console.log('statusCode', response && response.statusCode);
});
