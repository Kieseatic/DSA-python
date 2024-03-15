'''
#Selection sort
import time
import random
my_list =[random.randint(1, 1000) for _ in range(1000)]

def selectionSort(lst):
    n = len(lst)

    for i in range(n - 1):
        curr_min = i
        for j in range(i + 1, n):
            if lst[j] < lst[curr_min]:
                curr_min = j

        lst[i], lst[curr_min] = lst[curr_min], lst[i]

start = time.time()

print("Original list:", my_list)

selectionSort(my_list)

end = time.time()

print("Sorted list:", my_list)
print("Time taken: {:.6f} seconds".format(end - start))
'''

















#selection sort 
import random

random_numbers = [random.randint(1, 100) for _ in range(20)]

def selectionSort(list):
    for i in range(len(list) - 1):
        currMin = i
        for j in range(i + 1, len(list)):
            if list[j] < list[currMin]:
                currMin = j
        list[i], list[currMin] = list[currMin], list[i]

selectionSort(random_numbers)

print("Sorted list:", random_numbers)








