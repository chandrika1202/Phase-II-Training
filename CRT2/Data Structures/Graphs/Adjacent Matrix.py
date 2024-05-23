#Constructing Adjacency matrix 
n, m = map(int, input().split())  #n-nodes,m-edges
adj = [] 
for i in range(n + 1):
    eachRow = [0] * (n + 1)
    adj.append(eachRow)
 
for i in range(m):
    u, v = map(int, input().split())
    adj[u][v] = 1
    adj[v][u] = 1
 
print(adj)


#Constructing Adjacency List
n,m=map(int,input().split())  #n-nodes,m-edges
adj = [] 
for i in range(n + 1):
    adj.append([])
 
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
 
print(adj)

