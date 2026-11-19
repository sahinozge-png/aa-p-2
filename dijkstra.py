import heapq

def build_graph(N):
    adj = {i: [] for i in range(1, N + 1)}
    for i in range(1, N + 1):
        for j in range(max(1, i - 3), min(N + 1, i + 4)):
            if i != j:
                weight = i + j
                adj[i].append((j, weight))
    return adj

def dijkstra(N, S, D):
    repetitions = 0
    adj = build_graph(N)
    repetitions += N
    
    distances = {i: float('inf') for i in range(1, N + 1)}
    repetitions += N
    
    parent = {i: None for i in range(1, N + 1)}
    repetitions += N
    
    distances[S] = 0
    repetitions += 1
    
    pq = [(0, S)]
    repetitions += 1
    
    while pq:
        repetitions += 1
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > distances[u]:
            continue
            
        if u == D:
            break
            
        for v, weight in adj[u]:
            repetitions += 1
            distance = current_dist + weight
            
            if distance < distances[v]:
                distances[v] = distance
                parent[v] = u
                heapq.heappush(pq, (distance, v))
                repetitions += 1

    path = []
    curr = D
    while curr is not None:
        repetitions += 1
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    repetitions += len(path)
    
    if distances[D] == float('inf'):
        return [], float('inf'), repetitions
        
    return path, distances[D], repetitions