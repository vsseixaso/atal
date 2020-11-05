# https://www.geeksforgeeks.org/traveling-salesman-problem-using-branch-and-bound-2/

import math

MAX_N = float('inf')

def copy_to_final(curr_path):
	final_path[:N + 1] = curr_path[:]
	final_path[N] = curr_path[0]

def first_min(adj, i):
	min = MAX_N
	for k in range(N):
		if adj[i][k] < min and i != k:
			min = adj[i][k]

	return min

def second_min(adj, i):
	first, second = MAX_N, MAX_N
	for j in range(N):
		if i == j:
			continue
		if adj[i][j] <= first:
			second = first
			first = adj[i][j]
		elif(adj[i][j] <= second and adj[i][j] != first):
			second = adj[i][j]

	return second

def tsp_rec(adj, curr_bound, curr_weight, lvl, curr_path, vis):
	global final_res
	
	if lvl == N:
		if adj[curr_path[lvl - 1]][curr_path[0]] != 0:
			curr_res = curr_weight + adj[curr_path[lvl - 1]][curr_path[0]]
			if curr_res < final_res:
				copy_to_final(curr_path)
				final_res = curr_res
		return

	for i in range(N):
		if (adj[curr_path[lvl-1]][i] != 0 and vis[i] == False):
			temp = curr_bound
			curr_weight += adj[curr_path[lvl - 1]][i]

			if lvl == 1:
				curr_bound -= ((first_min(adj, curr_path[lvl - 1]) +
								first_min(adj, i)) / 2)
			else:
				curr_bound -= ((second_min(adj, curr_path[lvl - 1]) +
								first_min(adj, i)) / 2)

			if curr_bound + curr_weight < final_res:
				curr_path[lvl] = i
				vis[i] = True
				
				tsp_rec(adj, curr_bound, curr_weight,
					lvl + 1, curr_path, vis)

			curr_weight -= adj[curr_path[lvl - 1]][i]
			curr_bound = temp

			vis = [False] * len(vis)
			for j in range(lvl):
				if curr_path[j] != -1:
					vis[curr_path[j]] = True

def tsp(adj):
	curr_bound = 0
	curr_path = [-1] * (N + 1)
	vis = [False] * N

	for i in range(N):
		curr_bound += (first_min(adj, i) + second_min(adj, i))

	curr_bound = math.ceil(curr_bound / 2)

	vis[0] = True
	curr_path[0] = 0

	tsp_rec(adj, curr_bound, 0, 1, curr_path, vis)


N=5
adj = [[0, 3, 1, 5, 8],
       [3, 0, 6, 7, 9],
       [1, 6, 0, 4, 2],
       [5, 7, 4, 0, 3],
       [8, 9, 2, 3, 0]]
final_path = [None] * (N + 1)
vis = [False] * N
final_res = MAX_N

tsp(adj)

print("Minimum cost :", final_res)
print("Path Taken : ", end = ' ')
for i in range(N + 1):
	print(final_path[i], end = ' ')