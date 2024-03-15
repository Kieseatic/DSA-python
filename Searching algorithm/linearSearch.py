
import time 

my_list = [1, 2, 4, 5, 2, 6, 7]
target_value = 6

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

result = linear_search(my_list, target_value)
rec=time.time()


if result != -1:
    print(f'Target value {target_value} found at index {result+1}.')
else:
    print(f'Target value {target_value} not found in the list.')
print(rec)
