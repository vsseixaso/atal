# https://codeforces.com/problemset/problem/796/A

n, m, k = map(int, input().split())
h = list(map(int, input().split()))

dist = 105
for i in range(len(h)):
    if h[i] > 0 and h[i] <= k:
        dist = min(dist, abs(m-1-i))

print(dist * 10)