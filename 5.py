import numpy as np
import random

a = list()
for i in range(3):
    a.append([random.randint(-100, 100) for j in range(3)])
print("Матрица:")
print(np.array(a))
print("Транспонированная матрица:")
print(np.transpose(a))
