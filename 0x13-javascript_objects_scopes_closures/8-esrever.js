#!/usr/bin/node
exports.esrever = function (list) {
  const newArray = [];

  for (let i = list.length - 1; i >= 0; i--) {
  // push is the append in javascript
    newArray.push(list[i]);
  // newArra[counter] = list[i];
  // counter++
  }
  return newArray;
};
