n, m = map(int, input().split())
a = [-1] * (n+10)
b = [-1] * (n+10)

tmp = list(map(int, input().split()))
for i in range(1, n+1):
    a[i] = tmp[i-1]

s = set()
for i in range(n, -1, -1):
    s.add(a[i])
    b[i] = len(s)
    
for i in range(m):
    l = int(input())
    print(b[l])