n = int(input())
arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

for i in range(1, n):
    arr[i][0] += max(arr[i-1][1], arr[i-1][2])
    arr[i][1] += max(arr[i-1][0], arr[i-1][2])
    arr[i][2] += max(arr[i-1][0], arr[i-1][1])
    
print(max(arr[-1]))