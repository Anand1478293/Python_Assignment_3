# Implementing function to calculate factorial of given number using recursion

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
    
#  Taking an Intiger value from the user and also implement function calling

num = int(input('Enter an interger value: '))
result = factorial(num)

# printing result of given number by the user

print('The factorial of given number is: ',result)