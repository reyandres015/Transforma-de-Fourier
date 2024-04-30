import numpy as np
import matplotlib.pyplot as plt

# Generate a linspace of 1 to 10
x = np.linspace(1, 10, 500)

# Define the different functions for the machine vibrations
y1 = np.sin(2 + x)  # Simple sine wave
y2 = np.cos(3 * np.pi * x)  # Simple cosine wave
y3 = np.exp(-x / 5)  # Exponential decay

# Combine the functions to create the signal
y = y1 + y2 + y3

# Plot the signal
plt.plot(x, y)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Signal for resolving with Fourier")
plt.show()