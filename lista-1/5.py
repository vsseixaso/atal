def valid(i, j, tab, vis):
    if i >= 5 or j >= 5 or i < 0 or j < 0:
        return False
    return not vis[i][j] and tab[i][j] != 1

def find(i, j, tab, vis):
    if not valid(i, j, tab, vis):
        return

    vis[i][j] = True

    find(i+1, j, tab, vis)
    find(i-1, j, tab, vis)
    find(i, j+1, tab, vis)
    find(i, j-1, tab, vis)

def has_way(ini, fim, tab, vis):
    find(ini[0], ini[1], tab, vis)
    return vis[fim[0]][fim[1]]


ini = list(map(int, input().split()))
fim = list(map(int, input().split()))

tab = []
vis = [[False for n in range(5)] for m in range(5)]

for i in range(5):
    row = list(map(int, input().split()))
    tab.append(row)
  
print(has_way(ini, fim, tab, vis))