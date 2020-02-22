import numpy as np
import matplotlib.pyplot as plt
import random
import math as m


N = 100
K = 10

def polynom(x, theta):
    # Polynom with coefficients list theta
    # Jedi way
    #return sum([theta[i] * cos(x*i) for i in range(((len(theta)-1)/2)+1),theta[i+len(theta)/2] * sin(x*i) for i in ((len(theta)-1)/2)+1])
    # Noob way
	result = 0
	for i in range(K+1):
		result += theta[i] * m.cos(x*i)
	for i in range(K+1,2*K+1):
		result += theta[i] * m.sin(x*i)
	return result

# Generate sample
a, b = -3, 3
theta = [random.uniform(-1, 1) for i in range(2*K + 1)]
xs = [random.uniform(a, b) for i in range(N)]
ys = [polynom(x, theta) + random.uniform(-1, 1) for x in xs]
#ys=list(map(lambda x: 1 if x >= 0 else -1,xs))
print(theta)
plt.plot(xs, ys, "o")

# Estimate theta

K=2

X=[]
for i in range(N):
	X.append([])
	for j in range(K+1):
		X[i].append(m.cos(xs[i]*j))
	for j in range(K+1,2*K+1):
		X[i].append(m.sin(xs[i]*j))

X = np.array(X)
y = np.array(ys)
# Overflow...
theta = np.linalg.inv(X.T @ X) @ X.T @ y
# Good solution
#theta = np.linalg.lstsq(X, y, rcond=None)[0]

print(theta)

# Draw estimated curve
xs_draw = np.arange(a, b, 0.01)
ys_draw = [polynom(x, theta) for x in xs_draw]
plt.plot(xs_draw, ys_draw)

plt.xlabel("x")
plt.ylabel("y")
plt.show()
