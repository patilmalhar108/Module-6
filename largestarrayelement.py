print("Write code to find the largest number in the list recursivly")
def largest_element(a):
    length = len(a)
    if length == 1:
        return a[0]
    return max(a[0],largest_element(a[1:]))

a = [1,2,56,79,199,330,27,313]
print("Largest element of array is:",largest_element(a))