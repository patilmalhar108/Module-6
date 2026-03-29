def reverse_string(s):
    if len(s) == 1:
        return s[0]
    firstchar = s[0]
    return reverse_string(s[1:]) + firstchar

s = "Hello"
print("Reverse string is =",reverse_string(s))