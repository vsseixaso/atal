n = int(input())
a = list(map(int, input().split()))

a.sort()

sum = 0
for i in range(n):
    sum += a[i]
sum /= 2

cnt = 0
ans = 0
while ans <= sum:
    cnt += 1
    ans += a[n-cnt]

print(cnt)