import numpy as np

f_sin = lambda x, y: np.sin(x)
f1 = lambda x, y: x*y
z = lambda x, y: x ** 2 - y

f_sin_true = lambda x: 2 - np.cos(x)
f1_true = lambda x: np.e ** (x * x / 2)
z_true = lambda x: np.e ** (-x) + x ** 2 - 2 * x + 2
