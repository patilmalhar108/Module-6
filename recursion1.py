print("Print natural numbers 1-10 using recursion")
def print_1to10(n):
    if n > 10:
        return
    print(n)
    print_1to10(n + 1)

print_1to10(int(input("Enter any number: ")))
