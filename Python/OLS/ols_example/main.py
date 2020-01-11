"""
An example of ordinary least squares regression.
"""

from typing import Tuple
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# hack to handle relative imports when package isn't installed
try:
    import linalg as la
except:
    from ols_example import linalg as la

matmul = la.matmul
invert = la.invert_matrix
transpose = la.transpose

def read_data(path: str) -> Tuple[np.ndarray, np.ndarray]:
    df = pd.read_csv(path)
    x = df.features.values
    y = df.targets.values
    return x, y

def set_dimensions(arr: np.ndarray) -> np.ndarray:
    if len(arr.shape) == 3:
        return arr
    if len(arr.shape) == 1:
        return arr.reshape(-1, 1)
    if len(arr.shape) > 2:
        raise Exception("Too many dimensions.")
    raise Exception("Too few dimensions.")

def append_ones(arr: np.ndarray) -> np.ndarray:
    return np.append(arr, np.ones([len(arr), 1]), 1)

def fit_ols(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    alpha = matmul( transpose(X), X)
    beta = matmul( transpose(X), y)
    return matmul( invert(alpha), beta )

def rmse(y_true, y_pred):
    """
    """
    squared_error = (y_true - y_pred)**2.0
    mean_squared_error = np.mean(squared_error)
    return mean_squared_error**0.5

if __name__ == "__main__":

    # an example of the functions in this module

    x = np.random.uniform(0, 10, 100)
    y = 1.2 * x + np.random.normal(0, 1, 100)
    x, y = set_dimensions(x), set_dimensions(y)
    x = append_ones(x)
    beta = fit_ols(x, y)
    predictions = x.dot(beta)

    print("Root Mean Squared Error: {}".format(rmse(y, predictions)))

    plt.figure(figsize=(8, 8))
    plt.scatter(x[:, 0], y)
    plt.scatter(x[:, 0], predictions)
    plt.show()
