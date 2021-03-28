# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import mergeSort
import karatsuba
import invertedCounter
import strassenMultiplication
import closestPairInAPlane

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # array = [1, 4, 2, 6, 8, 5, 6, 3, 9, 10, 11, 53, 22, 1, 3, 5, 3]
    # f(mergeSort.merge_sort(array))
    # print(karatsuba.Karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
    #                           2718281828459045235360287471352662497757247093699959574966967627))
    f = open("IntegerArray.txt", "r")
    # print(f.read())
    print(invertedCounter.total_count(f.readlines()))
    # print(strassenMultiplication.strassen(np.array([[2, 4], [3, 5]]), np.array([[5, 3], [6, 8]])))
    P = [closestPairInAPlane.Point(2, 3), closestPairInAPlane.Point(12, 30),
         closestPairInAPlane.Point(11, 10),
         closestPairInAPlane.Point(40, 50), closestPairInAPlane.Point(5, 4),
         closestPairInAPlane.Point(12, 10), closestPairInAPlane.Point(3, 4)]
    closestPairInAPlane.closest(P)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
