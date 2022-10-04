#!/usr/bin/node
const args = process.argv;
const pathA = args[2];
const pathB = args[3];
const pathC = args[4];

const fs = require('fs').promises;

async function readFile (filePath) {
  try {
    const data = await fs.readFile(filePath);
    return (data.toString());
  } catch (error) {
    console.error(`Got an error trying to read the file: ${error.message}`);
  }
}

const dataOne = readFile(pathA);
const dataTwo = readFile(pathB);
const output = dataOne + dataTwo;
console.log(output);
console.log(pathC);
