def divid(s):
    n = len(s)
    if n % 2:
        return s
    
    n = int(n / 2)
    s1 = divid(s[:-n])
    s2 = divid(s[n:])
    
    if s1 > s2:
        return s1 + s2
    else:
        return s2 + s1


a = input()
b = input()

if divid(a) == divid(b):
    print("YES")
else:
    print("NO")