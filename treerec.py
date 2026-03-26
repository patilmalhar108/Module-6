def treerec(n):
    if n != 0:
        print(n)
        treerec(n - 1)
        treerec(n - 1)

treerec(2)