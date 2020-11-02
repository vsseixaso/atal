def troca(a, b):
    sum_a = sum(a)
    sum_b = sum(b)
    if sum_a == sum_b:
        return []
    
    for i in range(len(a)):
        for j in range(len(b)):
            new_sum_a = sum_a - a[i] + b[j]
            new_sum_b = sum_b + a[i] - b[j]
            if new_sum_a == new_sum_b:
                return [a[i], b[j]]
            
    return []

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(" ".join(str(e) for e in troca(a, b)))

# complexidade: O(n*m)