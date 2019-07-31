const stats = require('./stats');
var assert = require('assert');

console.log("Stats Test Package");

var arr = [1,2,3,4,5,6,7,8,9,10];

assert(stats.max(arr) == 10);
assert(arr.max(arr) == 10);
assert(stats.min(arr) == 1);
assert(arr.min(arr) == 1);
assert(arr.range(arr) == 9);
assert(arr.sum(arr) == 55);
assert(arr.mean(arr) == 5.5);

var arr = [9,8,7,6,5]

assert(arr.median(arr) == 7);

var arr = [14,15,16,17,18,19]

assert(arr.median(arr) == 16.5);

var arr = ['a',2,3,4,5,6,7,8,9,10];

try {
  arr.max();
}
catch(err) {
  assert(err == "Array contains non-numerics!")
}

var arr = 'a'

try {
  stats.max(arr);
}
catch(err) {
  assert(err == "Not an Array!")
}

console.log("Tests Complete. No Errors.");
