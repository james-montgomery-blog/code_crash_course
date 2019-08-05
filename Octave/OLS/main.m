source("utils.m")

[x, y]  = read_data("../../Test_Data/linear.csv");

x = append_ones(x);
beta = inv(x' * x) * (x' * y);

predictions = x * beta ;

f = figure
hold on;
scatter(y, x(:, 2), "b");
plot(predictions, x(:, 2), "r");
hold off;
waitfor(f)
