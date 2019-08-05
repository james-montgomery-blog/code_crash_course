
addpath(pwd)
function [x, y] = read_data (path)
  data = csvread(path);
  x = data(2:end, 2);
  y = data(2:end, 3);
  return;
endfunction

function arr = append_ones (arr)
  arr = [ones(size(arr, 1), 1) arr];
  return;
endfunction
