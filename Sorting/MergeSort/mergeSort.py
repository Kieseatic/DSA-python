#Merge sort
def mergeSort(arr):
    if len(arr) > 1: 
        left_arr = arr[:len(arr) //2]    #aage se mid
        right_arr = arr[len(arr)//2:]    #piche se mid 

        #recursion
        mergeSort(left_arr)
        mergeSort(right_arr)  

        #merge 
        i = 0  #left array index
        j = 0  #right array index
        k = 0  #merge array index

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else: 
                arr[k] = right_arr[j]
                j+=1
            k+=1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1 

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1


array= [2,3,5,4,1,7,6,8,10,9]
mergeSort(array)
print("Sorted array:", array)

