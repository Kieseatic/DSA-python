'''
def evenNums(num):
    print("The even numbers are: ", num);
    while(num % 2 ==0):
        
        if num == 2:
            return num
        else:
            return evenNums(num-2)
    
evenNums(9)
'''
'''

# factorial without recursion 
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Example usage
result = factorial_iterative(5)
print("Factorial of 5:", result)

    '''

#factorial with recursion
    

def factorial(num):
    
    if num == 1 or num == 0:
        return 1 
    
return num*factorial(num -1)