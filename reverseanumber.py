def reverse_number(number):
    if number > 0:
        last = number % 10
        if number // 10 > 0:
            current_number = reverse_number((int)(number // 10))
            return last * pow(10, len(str(current_number))) + current_number
        return number
    
n = int(input("Enter your number: "))
print("Reverse number is =",reverse_number(n))