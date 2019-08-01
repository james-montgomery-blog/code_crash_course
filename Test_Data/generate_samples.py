import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Linear Example

features = np.random.uniform(-10, 10, 100)
targets = features * 2.4 + 7.1 + np.random.normal(0, 7, 100)
df = pd.DataFrame({
    "features": features,
    "targets": targets
})
df.to_csv("linear.csv")

# Linear Example

features = np.random.uniform(-10, 10, 100)
targets = features**3 + 7.1 + np.random.normal(0, 150, 100)
df = pd.DataFrame({
    "features": features,
    "targets": targets
})
df.to_csv("nonlinear.csv")
