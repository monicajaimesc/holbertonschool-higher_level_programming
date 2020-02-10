#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  let i;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      counter++;
    }
  }
  return counter;
};
