import numpy as np

import matplotlib.pyplot as plt

sigma = 4  # Standard deviation
n_samples = 10000

# Generate random samples from normal distribution
data = np.random.normal(loc=0, scale=sigma, size=n_samples)

# Plot histogram
plt.hist(data, bins=50, density=True, alpha=0.7, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title(f'Normal Distribution (σ={sigma})')
plt.grid(True, alpha=0.3)
plt.show()