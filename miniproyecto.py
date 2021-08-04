from scipy.stats import uniform
import matplotlib.pyplot as plt
import numpy as np


N = 10000

fig, ax = plt.subplots(1, 1)

mean, var, skew, kurt = uniform.stats(moments='mvsk')
print("Mu=", mean)
r = uniform.rvs(size=N)

ax.axhline(y=mean, color='r', label='Mu') # Mu line

s_n = [ np.mean(r[:i]) for i in range(len(r)) ]
ax.plot(s_n, label='n-->s_n')

ax.set(title='Teoría de los grandes números', xlabel='n', ylabel='Media aritmética')
ax.legend(loc='best')

plt.show()
