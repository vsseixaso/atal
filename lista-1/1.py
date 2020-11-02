def divisores(num):
    out = []
    for i in range(1, num//2 + 1):
        if num % i == 0:
            out.append(i)
    out.append(num)
    return out

n = int(input())
print(" ".join(str(e) for e in divisores(n)))

# complexidade: O(n)