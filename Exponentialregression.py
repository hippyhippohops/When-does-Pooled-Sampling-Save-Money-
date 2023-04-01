import numpy as np
import matplotlib.pyplot as plt
import math

def main():
    x = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    y = [3, 2.9, 2.7, 2.65, 2.42, 2.32, 1.98, 1.72, 1.48, 1.42, 0]
    y = [0, 1.42, 1.48, 1.72, 1.98, 2.32, 2.42, 2.65, 2.7, 2.9, 3]
    print(y)
    x_1 = [0.0,1.0]
    y_1 = [0.0,3.0]
    plt.scatter(x, y)
    plt.title("Average Number of Test vs Incidence Scatter Diagarm")
    plt.xlabel("Incidence")  # x label
    plt.ylabel("Average Number of Test")  # y label
    plt.plot(np.array(x), -1.0084 * np.array(x) ** 2 + 3.0105 * np.array(x) + 0.996)
    #plt.plot(x_1, y_1)

    plt.show()


main()
