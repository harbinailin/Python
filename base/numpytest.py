import numpy as np

a = np.repeat(np.arange(5).reshape([1, -1]), 10, axis=0) + 10.0
b = np.random.randint(5, size=a.shape)
c = np.argmin(a * b, axis=1)
b = np.zeros(a.shape)
b[np.arange(b.shape[0]), c] = 1
print(b)
