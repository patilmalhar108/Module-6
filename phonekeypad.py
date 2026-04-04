print("Printe all the possible combinations when we press 3 keys on the phone keypad")
keypad = ["","","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
def print_combinations(combination, curr, output, n):
    if curr == n:
        print(*output, sep = ",")
        return
    for i in range(len(keypad[combination[curr]])):
        output.append(keypad[combination[curr]][i])
        print_combinations(combination, curr + 1, output, n)
        output.pop()
        if (combination[curr] == 0 or combination[curr] == 1):
            return
        
combination = [4,3,4]
n = len(combination)
print_combinations(combination, 0, (), n)