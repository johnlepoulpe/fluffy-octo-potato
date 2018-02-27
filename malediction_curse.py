import numpy as np
import matplotlib.pyplot as plt

distinguishability = []

for i in range(6):
	n, r, d = 1000, 1000, 10**i

	X = np.random.randn(n,d) # Set of n vector of dimension d
	R = np.random.randn(r,d) # Set of r vector of dimension d

	normX = np.linalg.norm(X, axis = 1)**2 # Applies the square of the square norm on set X
	normR = np.linalg.norm(R, axis = 1)**2 # Applies the square of the square norm on set R

	scalar_product = np.dot(X,R.transpose()) # Computes the scalar product of X with tR
	distance = np.repeat(normX[:,np.newaxis], r, 1) + np.repeat(normR[np.newaxis,:], n, 0) - 2*scalar_product 
	# Computes the distance between each vector of R from those of X
	
	min = np.amin(distance, 0)
	max = np.amax(distance,0)
	remoteness = min/max
	distinguishability.append(np.mean(remoteness))

print(distinguishability)
plt.plot(distinguishability)
plt.show()
