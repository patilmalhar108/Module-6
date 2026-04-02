n = int(input("Enter a number to see if it a power of 2: "))
def check(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 == 0:
        return check(n / 2)
    return False

if (check(n)):
    print("Power of 2")
else:
    print("Not a power of 2")