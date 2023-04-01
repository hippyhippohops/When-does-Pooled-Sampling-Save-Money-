import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    distribution_of_pool_samples = []
    average = []
    incidence = []

    for x in range(0,121):
        for y in range(0, 120-x):
            z = 120-x-y
            distribution_of_pool_samples.append((x,y,z))
            average.append((x + 2 * y + 3 * z)/120)
            incidence.append((y + 2 * z)/240)

            distribution_of_pool_samples.append((x, z, y))
            average.append((x + 2 * z + 3 * y) / 120)
            incidence.append((z + 2 * y) / 240)

            distribution_of_pool_samples.append((y, x, z))
            average.append((y + 2 * x + 3 * z) / 120)
            incidence.append((x + 2 * z) / 240)

            distribution_of_pool_samples.append((y, z, x))
            average.append((y + 2 * z + 3 * x) / 120)
            incidence.append((z + 2 * x) / 240)

            distribution_of_pool_samples.append((z, x, y))
            average.append((z + 2 * x + 3 * y) / 120)
            incidence.append((x + 2 * y) / 240)

            distribution_of_pool_samples.append((z, y, x))
            average.append((z + 2 * y + 3 * x) / 120)
            incidence.append((y + 2 * x) / 240)

    data = {'Distribution of Pool Samples': distribution_of_pool_samples, 'Average Number of Test Cases': average}
    df = pd.DataFrame(data)
    #df.to_csv('Final_Average.csv')
    #print(df)
    x = np.array(incidence)
    y = np.array(average)

    plt.scatter(x, y)
    plt.title("Incidence vs Average Number of Test Required")
    plt.xlabel("Incidence (% of positive cases)")
    plt.ylabel("Average Number of Test Required")
    plt.show()


main()
