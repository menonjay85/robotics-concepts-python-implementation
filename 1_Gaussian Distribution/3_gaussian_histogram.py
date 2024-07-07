import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, fixed
import random

def gen_samples(n, mu, sigma):
    """Generate n samples of a gaussian distribution"""
    samples = sigma * np.random.randn(n) + mu
    return samples

def hist_slice(samples, n):
    """Plot histogram for the first n values in samples"""
    plt.figure(figsize=(10, 6))
    # Plot histogram with the first n values
    plt.hist(samples[:n], bins=30, edgecolor='black', density=True, stacked=True)
    # Additional plot for Gaussian PDF
    x = np.linspace(min(samples), max(samples), 100)
    variance = 2 ** 2
    pdf = (1 / np.sqrt(2 * np.pi * variance)) * np.exp(-0.5 * ((x - 2) ** 2) / variance)
    plt.plot(x, pdf, 'r', label='Gaussian PDF (mu=2, sigma=2)')
    plt.xlabel("Sample Values")
    plt.ylabel("Density")
    plt.title(f"Histogram of First {n} Samples with Gaussian PDF Overlay")
    plt.legend()
    plt.show()

# Initialize seed and generate samples
random.seed(0)
samples = gen_samples(1000, 2, 2)

# Use Jupyter interact function for interactive histogram visualization
def interactive_hist(n):
    hist_slice(samples, n)

interact(interactive_hist, n=(100, 1000, 100))
