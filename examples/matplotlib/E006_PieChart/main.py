import matplotlib.pyplot as plt


if __name__ == '__main__':
    languages = ['Kotlin', 'Python', 'Java', 'Go', 'Rust', 'C++']
    time = [15, 13, 2, 7, 1, 10]
    Explode = [0.1, 0.0, 0, 0, 0, 0]
    plt.pie(time, explode=Explode, labels=languages, shadow=True, startangle=42)
    plt.axis('equal')
    plt.legend(title='Programming Languages')
    plt.show()
