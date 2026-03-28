print("Write a code to see if a given array is shorted or not")
def sorted(a):
    length = len(a)
    if length == 1 or length == 0:
        return True
    return a[0] <= a[1] and sorted(a[1:])

a = [1,2,3,5,7,8]
if sorted(a):
    print("Given array is sorted")
else:
    print("Given array is not sorted")