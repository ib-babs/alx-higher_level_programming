#!/usr/bin/node
const processArgv = process.argv;
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
add(processArgv[2], processArgv[3]);
