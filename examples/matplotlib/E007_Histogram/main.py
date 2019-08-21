import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    plt.title("Histogram")
    plt.xlabel("Data")
    plt.ylabel("Frequency")
    plt.hist(np.random.randn(10_000), 100)
    plt.show()
