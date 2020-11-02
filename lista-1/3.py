def soma_produto(a):
    a.sort()
    out = 0
    for i in range (len(a)):
        out += (a[i] * i)
    return out

a = list(map(int, input().split()))
print(soma_produto(a))

# complexidade: O(n log n)
# com a lista ordenada garantimos que o maior valor será multiplicado pelo maior índice, 
# maximizando assim o valor final obtido