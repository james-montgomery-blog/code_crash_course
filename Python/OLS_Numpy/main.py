from typing import Tuple
import pandas as pd
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

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
    return inv(X.T.dot(X)).dot(X.T.dot(y))

if __name__ == "__main__":
    #x, y = read_data("../../Test_Data/linear.csv")
    x, y = read_data("../Test_Data/linear.csv")
    x, y = set_dimensions(x), set_dimensions(y)
    x = append_ones(x)
    beta = fit_ols(x, y)
    predictions = x.dot(beta)

    plt.scatter(x[:, 0], y)
    plt.scatter(x[:, 0], predictions)
    plt.show()
