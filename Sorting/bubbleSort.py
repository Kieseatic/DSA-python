# Bubble Sort
import time 
import random

my_list = [2,6,3,4,1,8,5]



def bubbleSort(lst):
    swapped = True    #flag

    while swapped:
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True

# Record the start time
start_time = time.time()

# Example usage:
print("Original list:", my_list)

bubbleSort(my_list)

# Record the end time
end_time = time.time()

print("Sorted list:", my_list)
print("Time taken: {:.6f} seconds".format(end_time - start_time))
