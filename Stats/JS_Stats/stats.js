// I decided to learn js and refresh my memory
// on how to build a stats library all in one shot.
// You can consider this by sandbox for trying
// stuff out.

// Sources
// http://javascript.cs.lmu.edu/notes/commandlinejs/
// https://stackoverflow.com/questions/1669190/find-the-min-max-element-of-an-array-in-javascript
// https://gist.github.com/Daniel-Hug/7273430
// https://simplestatistics.org/

// node
// process.exit()

// Define stats functions

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

// function max(arr) {
//   is_numeric_array(arr)
//   return Math.max.apply(null, arr)
// }

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

// function min(arr) {
//   is_numeric_array(arr)
//   return Math.min.apply(null, arr)
// }

function min(arr) {
  is_numeric_array(arr)
  var len = arr.length, min = Infinity;
  while (len--) {
    if (arr[len] < min) {
      min = arr[len];
    }
  }
  return min;
};

function range(arr) {
  is_numeric_array(arr)
  return max(arr) - min(arr)
}

function sum(arr) {
  is_numeric_array(arr)
  var arr_sum = 0;
  for( var i = 0; i < arr.length; i++ ){
    arr_sum += parseInt( arr[i], 10 );
  }
  return arr_sum
}

function mean(arr) {
  is_numeric_array(arr)
  return sum(arr) / arr.length
}

function median(arr) {
  is_numeric_array(arr)
  arr.sort()
  if (arr.length % 2 !== 0) {
    var i = Math.floor(arr.length/2)
    return arr[i]
  }
  var a = Math.floor(arr.length/2) -1
  var b = Math.floor(arr.length/2)
  return (arr[a] + arr[b]) / 2
}

// Add as native to array type

Array.prototype.max = function() {
  return max(this);
};

Array.prototype.min = function() {
  return min(this);
};

Array.prototype.range = function() {
  return range(this);
};

Array.prototype.sum = function() {
  return sum(this);
};

Array.prototype.mean = function() {
  return mean(this);
};

Array.prototype.median = function() {
  return median(this);
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
