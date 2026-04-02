def paranthesis(s,l,r,p,n):
    if p == 2 * n:
        for ss in s:
            print(ss,end = '')
        print("\n")
        return
    if l > r:
        s[p] = "}"
        paranthesis(s, l, r + 1, p + 1, n)
    if l < n:
        s[p] = "{"
        paranthesis(s, l + 1, r, p + 1, n)

n = int(input("Enter the number of paranthesis: "))
s = [""] * 2 * n
paranthesis(s, 0, 0, 0, n)