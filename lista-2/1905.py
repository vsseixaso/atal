def valid(i, j, tab, vis):
    if i >= 5 or j >= 5 or i < 0 or j < 0:
        return False
    return not vis[i][j] and tab[i][j] != 1

def find(i, j, tab, vis):
    if not valid(i, j, tab, vis):
        return

    vis[i][j] = 1

    find(i+1, j, tab, vis)
    find(i-1, j, tab, vis)
    find(i, j+1, tab, vis)
    find(i, j-1, tab, vis)


t = int(input())

for i in range(t):
    tab = []
    vis = [[0 for n in range(5)] for m in range(5)]

    while True:
        if len(tab) == 5: break
        else:
            aux = list(map(int, input().split()))
            if len(aux) > 0:
                tab.append(aux)
				
    find(0, 0, tab, vis)

    if vis[4][4]: print("COPS")
    else: print("ROBBERS")