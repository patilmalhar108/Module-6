#print("Find factorial of any number by using recursion")
def fact(n):
    if (n == 1 or n == 0):
        return 1
    return n * fact(n-1)

n = int(input("Enter any number to find its factorial: "))
print("Factorial of",n, "is equal to:",fact(n))