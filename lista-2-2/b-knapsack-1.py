def knapsack(dp, weight):
    arr = [0] * (weight+1)
    for i in range(len(dp)):
        for j in range(weight, dp[i][0]-1, -1):
            tmp = dp[i][1] + arr[j-dp[i][0]]
            if tmp > arr[j]:
                arr[j] = tmp
   
    return arr[weight]

n, w = [int(k) for k in input().split()]
dp = []
for i in range(n):
    dp += [[int(k) for k in input().split()]]

print(knapsack(dp, w))
