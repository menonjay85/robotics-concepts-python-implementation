# Create a function for a gaussian probability distribution with mean=2 and stand.dev=1 where x lies in [-5, 5]. 
# Generate 100 samples for the same.

import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets


def evaluate_gaussian(mu, sigma, min_interval, max_interval, n_samples):
    # Evaluates a gaussian distribution between in a certain interval and plots it
    plt.figure()
    x = np.linspace(min_interval, max_interval, n_samples)  # Create the array of values where the Gaussian distribution will be evaluated
    variance = sigma ** 2  # Get the variance from the given standard deviation
    res = (1 / np.sqrt(2 * np.pi * variance)) * np.exp(-0.5 * ((x - mu) ** 2) / variance)  # Implement the Gaussian distribution computation
    plt.plot(x, res)  # Show the results
    plt.title(f'Gaussian PDF: mu={mu}, sigma={sigma}')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.show()
    print(x)

"""
Args:        
mu: mean of the distribution
sigma: standard deviation of the distribution
min_interval: minimum value of the interval
max_interval: maximum value of the interval
n_samples: number of samples
"""

# Parameters
mu = 2
sigma = 1
min_interval = -5
max_interval = 5
n_samples = 100

# Function call to plot the Gaussian PDF
evaluate_gaussian(mu, sigma, min_interval, max_interval, n_samples)