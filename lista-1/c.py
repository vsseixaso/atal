# https://codeforces.com/problemset/problem/822/B

def add_one(x): return x + 1

n, m = map(int, input().split())
s = input()
t = input()

res = list(range(n))

for j in range(m - n + 1):
    new_res = []
    for i in range(n):
        if s[i] != t[i + j]:
            new_res.append(i)
    if len(new_res) < len(res):
        res = new_res

print(len(res))
print(*list(map(add_one, res)))