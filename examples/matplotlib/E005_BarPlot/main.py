import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    letters = ['A', 'B', 'C', 'D', 'F']
    marks = [90, 80, 75, 60, 30]
    boys_average = [83, 77, 70, 62, 45]

    index = np.arange(5)
    width = 0.2

    plt.bar(index, marks, width, color='green', label='Marks')
    plt.bar(index+width, boys_average, width, color='yellow', label='Average')
    plt.title("Bar Graphs")

    plt.xlabel("Letters")
    plt.ylabel("Marks")
    plt.xticks(index + width/2, letters)
    plt.legend(loc='best')
    plt.show()
