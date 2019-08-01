using CSV
using Plots
using DataFrames
using LinearAlgebra

# using REPL
# const output = IOBuffer()
# const out_terminal = REPL.Terminals.TerminalBuffer(output)
# const basic_repl = REPL.BasicREPL(out_terminal)
# const basic_display = REPL.REPLDisplay(basic_repl)
# Base.pushdisplay(basic_display)
# plotly()

function read_data(path::String)
    dataframe = CSV.read(path)
    x::Array = dataframe.features
    y::Array = dataframe.targets
    return x, y;
end

function set_dimensions(arr::Array)
    if length(size(arr)) == 2
        return arr;
    elseif length(size(arr)) == 1
        return reshape(arr, (:, 1));
    elseif length(size(arr)) > 2
        throw("Error")
    else
        throw("Error")
    end
end

function append_ones(arr::Array)
    one_arr = ones(size(x))
    return hcat(x, one_arr);
end

function fit_ols(X::Array, y::Array)
    return inv(transpose(X)*X)*(transpose(X)*y)
end

wait_for_key(prompt) = (print(stdout, prompt); read(stdin, 1); nothing)

x, y = read_data("../../Test_Data/linear.csv")
x, y = set_dimensions(x), set_dimensions(y)
x = append_ones(x)
beta = fit_ols(x, y)
predictions = x*beta

p1 = plot(x[:, 1], y, seriestype=:scatter, title="My Scatter Plot");
plot!(p1, x[:, 1], predictions);
display(p1)

wait_for_key("Press any key to continue...")
