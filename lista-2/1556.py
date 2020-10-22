tamanho = 0
palavra = ['' for n in range(1005)]

def ord_to_chr(array):
    res = ''
    for item in array:
        res += chr(item)
    return res

def dfs(g, x):
    for i in range(30):
        if g[x][i]:
            global tamanho
            global palavra
            
            palavra[tamanho] = ord('a') + i
            tamanho += 1
            print(ord_to_chr(palavra[:tamanho]))
            dfs(g, g[x][i])
            tamanho -= 1

while True:
    try:
        en = 'X' + input()
        g = [[0 for n in range(30)] for m in range(1005)]
        lig = [0 for n in range(30)]
        
        for i in range(len(en)-1, -1, -1):
            for j in range(len(lig)):
                g[i][j] = lig[j]

            lig[ord(en[i]) - ord('a')] = i
            
        tamanho = 0
        dfs(g, 0)
        print()

    except EOFError:
        break