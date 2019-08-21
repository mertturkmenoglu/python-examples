import matplotlib.pyplot as plt

if __name__ == '__main__':
    letters = ['A', 'B', 'C', 'D', 'F']
    marks = [90, 80, 75, 60, 30]
    variance = [5, 4, 2, 10, 15]

    plt.barh(letters, marks, xerr=variance, color='red')
    plt.title("Bar")
    plt.xlabel("Marks")
    plt.ylabel("Letters")
    plt.show()
