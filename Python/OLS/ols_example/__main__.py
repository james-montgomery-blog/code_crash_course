import linalg
import main
import matplotlib.pyplot as plt

x, y = main.read_data("../Test_Data/linear.csv")
x, y = main.set_dimensions(x), main.set_dimensions(y)
x = main.append_ones(x)
beta = main.fit_ols(x, y)
predictions = linalg.matmul(x, beta)

print("Root Mean Squared Error: {}".format(main.rmse(y, predictions)))

plt.figure(figsize=(8, 8))
plt.scatter(x[:, 0], y)
plt.scatter(x[:, 0], predictions)
plt.show()
