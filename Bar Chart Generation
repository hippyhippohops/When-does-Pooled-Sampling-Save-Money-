import matplotlib.pyplot as plt

def main():
    test_1_sample_number, test_2_sample_number, test_3_sample_number = map(int,input().split())

    x_axis = ['1', '2', '3']
    y_axis = [test_1_sample_number, test_2_sample_number, test_3_sample_number]
    average_no_of_samples = (test_1_sample_number + test_2_sample_number * 2 + test_3_sample_number * 3)/120

    plt.bar(x_axis, y_axis)
    plt.title('Testing Results (%s)' % round(average_no_of_samples,2))
    plt.xlabel('Number of tests')
    plt.ylabel('Number of Pairs of Samples')
    plt.show()

main()
