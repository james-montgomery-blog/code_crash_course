
function is_numeric_array(arr) {
  if (arr.constructor !== Array){
    throw "Not an Array!";
  }
  if (arr.length <= 1){
    throw "Array length <= 1!";
  }
  for (i = 0; i < arr.length; i++) {
    if (typeof arr[i] !== "number"){
    throw "Array contains non-numerics!";
    }
  }
}

function max(arr) {
  is_numeric_array(arr)
  var len = arr.length, max = -Infinity;
  while (len--) {
    if (arr[len] > max) {
      max = arr[len];
    }
  }
  return max;
};

// define exports

module.exports = {
  max: function(arr) {
     return max(arr);
  },
  min: function(arr) {
     return min(arr);
  },
}
