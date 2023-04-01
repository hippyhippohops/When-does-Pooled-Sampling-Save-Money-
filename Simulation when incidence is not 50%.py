import random
import matplotlib.pyplot as plt


def main():
    incidence = float(input("Please enter the incidence, as a decimal between 0 and 1"))
    n = 10000
    collection_of_data = []
    for i in range(0,n):
        test_results_for_pair_of_student = []
        test_results_for_pair_of_student.append(round(random.uniform(0,1), 2))
        test_results_for_pair_of_student.append(round(random.uniform(0,1), 2))
        collection_of_data.append(test_results_for_pair_of_student)
    pooled_sample_result = []
    number_of_test_for_each_sample = []
    for i in collection_of_data:
        if i[0] < incidence and i[1] < incidence:
            pooled_sample_result.append("Negative")
            number_of_test_for_each_sample.append(1)
        else:
            pooled_sample_result.append("Positive")
            index_of_selected_student = random.randint(0,1)
            if i[index_of_selected_student] < incidence:
                number_of_test_for_each_sample.append(2)
            else:
                number_of_test_for_each_sample.append(3)
    print(collection_of_data)
    print(pooled_sample_result)
    print(number_of_test_for_each_sample)

    test_1_sample_number = number_of_test_for_each_sample.count(1)
    test_2_sample_number = number_of_test_for_each_sample.count(2)
    test_3_sample_number = number_of_test_for_each_sample.count(3)

    x_axis = ['1', '2', '3']
    y_axis = [test_1_sample_number, test_2_sample_number, test_3_sample_number]
    average_no_of_samples = (test_1_sample_number + test_2_sample_number * 2 + test_3_sample_number * 3) / n

    plt.bar(x_axis, y_axis)
    plt.title('Testing Results (%s)' % round(average_no_of_samples, 2))
    plt.xlabel('Number of tests')
    plt.ylabel('Number of Pairs of Samples')
    plt.show()

main()
