cases = int(input())
 
for c in range(cases):
    aux = []
    aux2 = []
    
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    
    ans = 0
    
    for j in range(30, -1, -1):
        
        qtde = 0
        bit = 1 << j
        
        for i in range(len(v)-1, -1, -1):
            
            if bit & v[i]:
                qtde += 1
                aux.append(i)
            else:
                aux2.append(i)
                
        if qtde >= k:
            aux_ans = v[aux[0]]
            
            for i in range(1, qtde):
                aux_ans = aux_ans & v[aux[i]]
                
            ans = max(ans, aux_ans)
            
            for i in range(len(aux2)):
                v.pop(aux2[i])
                
        aux = []
        aux2 = []
        
    print(ans)
    v = []