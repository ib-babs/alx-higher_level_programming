#!/usr/bin/node
const processArgv = process.argv;
const firstArg = parseInt(processArgv[2]);

if (processArgv.length < 3) console.log(0);
else if (processArgv.length === 3) console.log(0);
else {
  let holder = firstArg;
  let holder2;

  for (let index = 2; index < processArgv.length; index++) {
    if (holder < parseInt(processArgv[index])) {
      holder2 = holder;
      holder = parseInt(processArgv[index]);
    }
  }
  console.log(holder2);
}
