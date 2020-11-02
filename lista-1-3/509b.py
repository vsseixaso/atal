imin = 105
imax = -105

n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    if a[i] > imax: imax = a[i]
    if a[i] < imin: imin = a[i]

if (imax - imin) > k:
    print("NO")
else:
    print("YES")
    for i in range(n):
        out = []
        for j in range(a[i]):
            out.append(j % k + 1)
        print(" ".join(str(e) for e in out))
        
            