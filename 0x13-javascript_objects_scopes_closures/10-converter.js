#!/usr/bin/node

exports.converter = function (base) {
  // function(n) is execute in the return of function (base)
  return function (n) {
    return n.toString(base);
  };
};
