t = int(input())

for i in range(t):
    n, k = list(map(int, input().split()))

    ini = k // (n-1) * n
    if k % (n-1) == 0:
        temp = -1
    else:
        temp = k % (n-1)
    ini += temp

    print(ini)