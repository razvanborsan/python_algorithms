# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import mergeSort
import karatsuba


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    array = [1, 4, 2, 6, 8, 5, 6, 3, 9, 10, 11, 53, 22, 1, 3, 5, 3]
    print(mergeSort.merge_sort(array))
    print(karatsuba.Karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
                              2718281828459045235360287471352662497757247093699959574966967627))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
