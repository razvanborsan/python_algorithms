# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import mergeSort
import karatsuba
import invertedCounter
import strassenMultiplication


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # array = [1, 4, 2, 6, 8, 5, 6, 3, 9, 10, 11, 53, 22, 1, 3, 5, 3]
    # f(mergeSort.merge_sort(array))
    # print(karatsuba.Karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
    #                           2718281828459045235360287471352662497757247093699959574966967627))
    # print(invertedCounter.count_inversions([1, 3, 5, 2, 4, 6]))
    print(strassenMultiplication.strassen(np.array([[2, 4], [3, 5]]), np.array([[5, 3], [6, 8]])))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
