#without recurssion
def factorial(n):
    fact = 1
    if n==0 :
        return 1
    while n > 0 :
        fact = n * fact
        n = n-1
    return fact


n = int(input("enter a number : "))
factorial(n)
print(factorial(n))

#with recurssion
def factorial(n):
    
    if (n == 0 or n==1):
        return 1
    else :
        return n * factorial(n-1)


n = int(input("enter a number : "))
factorial(n)
print("factorial of ", n, "is",factorial(n))