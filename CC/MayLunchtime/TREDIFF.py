#Partial

def findMinDiff(arr, n): 
    arr = sorted(arr) 
  
    diff = 10**20
  
    for i in range(n-1): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i+1] - arr[i] 
    return diff

def bfs(graph_to_search, start, end):
    queue = [[start]]
    visited = set()

    while queue:
        path = queue.pop(0)

        vertex = path[-1]

        if vertex == end:
            return path
        elif vertex not in visited:
            for current_neighbour in graph_to_search.get(vertex, []):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)

            visited.add(vertex)

for t in range(int(input())):
    N,Q=map(int,input().split())
    tree=list(map(int,input().split()))
    tree.insert(0,0)
    nodes = list(range(N+1))
    nodes.pop(0)
    graph = {k: [] for k in range(N+1)}
    graph.pop(0)
    for i in range(N-1):
        e1,e2=map(int,input().split())
        graph[e1].append(e2)
        graph[e2].append(e1)
    for i in range(Q):
        s,d=map(int,input().split())
        path=bfs(graph, s, d)
        l=[]
        n=len(path)
        for j in range(n):
            l.append(tree[path[j]])


        print(findMinDiff(l,n))

        #print(min(abs(x-y) for x,y in zip(l,l[1:])))
