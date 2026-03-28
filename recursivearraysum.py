def totalsum(a):
    length = len(a)
    if length == 1:
        return a[0]
    return a[0] + totalsum(a[1:])

a = [1,2,4,6,7,8]
print("Array total sum is =",totalsum(a))