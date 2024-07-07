# Sample a gaussian distribution with mean = 2 & stand.dev = 2. Then plot the resulting values along the x axis.

import numpy as np
import matplotlib.pyplot as plt

def gen_samples(n, mu, sigma):
    # Generate n samples of a gaussian distribution
    samples = sigma * np.random.randn(n) + mu  # Scale and shift
    return samples

"""
Args:
    n: Number of samples
    mu: mean of the distribution
    sigma: standard deviation of the distribution

Returns:
    array of samples
"""

# Parameters
num = 100
mu = 2
sigma = 1

# Generate samples and plot
samples = gen_samples(num, mu, sigma)
plt.scatter(samples, np.zeros(num), alpha=0.5)  # alpha for better visibility if points overlap
plt.title('Gaussian Samples Along X-axis')
plt.xlabel('Sample value')
plt.yticks([])  # Hide y-axis as it's not relevant in this plot
plt.show()

# Second way to show
plt.scatter(gen_samples(num, mu, sigma), np.zeros(num))
plt.show()