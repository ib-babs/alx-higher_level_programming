#!/usr/bin/node

const list = require('./100-data').list;

const newArray = [];
list.map((data, index) => {
  newArray[index] = data * index;
  return newArray;
});
console.log(list);
console.log(newArray);
