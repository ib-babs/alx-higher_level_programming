#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  let i = 0;
  for (let index = list.length - 1; index >= 0; index--) { newList[i++] = list[index]; }
  return newList;
};
