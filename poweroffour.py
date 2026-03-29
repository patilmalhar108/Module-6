n = int(input("Enter a number to see if it a power of 4: "))
def check(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 4 == 0:
        return check(n / 4)
    return False

if (check(n)):
    print("Power of 4")
else:
    print("Not a power of 4")