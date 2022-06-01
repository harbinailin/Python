import numpy as np
import matplotlib.pyplot as plt
from time import time
import math


# def normfun(x, mu, sigma):
#     pdf = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
#     return pdf


def raylifun(x, mu, sigma):
    pdf = x * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / sigma ** 2
    return pdf


startTime = time()
xaxis = np.linspace(-10, 10, 200)
miu = 0
delta = 1
np.random.seed(1)
N = 10000
rand1 = np.random.rand(N)
rand2 = np.random.rand(N)
y1 = np.arange(10000, dtype=float)
y2 = np.arange(10000, dtype=float)
for index, value in enumerate(rand1):
    a = (-2 * math.log(value))
    y1[index] = pow(a, 0.5)
    y1[index] = miu + delta * y1[index]
    for index, value in enumerate(rand2):
        y2[index] = y1[index] * math.sin(2 * math.pi * value)
        y2[index] = miu + delta * y2[index]
        break
# print(y1)
# print("#####################")
# print(y2)
# patches=plt.hist(y2,bins=100)
# plt.show()
patches2 = plt.hist(y1, bins=30)
plt.subplot(221)
patches = plt.hist(y1, bins=100)
plt.plot(patches[1][:-1], patches[0])
plt.xlabel("values")
plt.ylabel("frequency")

# plt.subplot(222)
# patches1 = plt.hist(y2, bins=100)
# plt.plot(patches1[1][:-1], patches1[0])
# plt.xlabel("values")
# plt.ylabel("frequency")

plt.subplot(222)
plt.scatter(patches2[1][:-1], patches2[0] / 1400)
plt.plot(patches2[1][:-1], patches2[0] / 1400)
plt.xlabel("values")
plt.ylabel("probability")
c = np.arange(0, 5, 0.1)
d = raylifun(c, 0, 1)
plt.plot(c, d, 'r--')

# plt.subplot(224)
# plt.scatter(patches1[1][:-1], patches1[0] / 800)
# plt.plot(patches1[1][:-1], patches1[0] / 800)
# plt.xlabel("values")
# plt.ylabel("probability")
# b = np.arange(-5, 5, 0.1)
# a = normfun(b, 0, 1)
# plt.plot(b, a, 'r--')
duratrion = time() - startTime
print(duratrion)
plt.show()
