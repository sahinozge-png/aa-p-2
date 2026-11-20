import heapq                                                                        # Import heapq for min-heap priority queue     | 1 time

def build_graph(N):                                                                 # Build adjacency list and count exact steps  | 1 time per call
    reps = 0                                                                        # Initialize graph build repetition counter   | 1 time
    adj = {i: [] for i in range(1, N + 1)}                                          # Create empty neighbor lists for N cities    | N times
    reps += N                                                                       # Count N dictionary initialization steps     | 1 time
    for i in range(1, N + 1):                                                       # Loop over each source city i (1 to N)       | N times
        for j in range(max(1, i - 3), min(N + 1, i + 4)):                           # Check candidate neighbors within |i-j|<=3   | <= 7N - 12 times
            reps += 1                                                               # Count each inner loop iteration             | <= 7N - 12 times
            if i != j:                                                              # Exclude self-loops (i != j)                 | <= 7N - 12 times
                weight = i + j                                                      # Compute edge weight w_ij = i + j            | E = 6N - 12 times
                adj[i].append((j, weight))                                          # Append directed edge (j, weight) to adj[i]  | E = 6N - 12 times
    return adj, reps                                                                # Return adjacency list and exact build reps  | 1 time

def dijkstra(N, S, D, trace=False):                                                 # Dijkstra shortest path with optional trace  | 1 time per call
    if not (1 <= S <= N and 1 <= D <= N):                                           # Validate S and D are within [1, N]          | 1 time
        raise ValueError(f"S and D must be between 1 and {N}.")                     # Raise clear error on invalid city input     | <= 1 time

    adj, repetitions = build_graph(N)                                               # Build graph and initialize rep counter      | 1 time
    distances = {i: float('inf') for i in range(1, N + 1)}                          # Initialize all shortest distances to inf    | N times
    repetitions += N                                                                # Count N distance initializations            | 1 time
    parent = {i: None for i in range(1, N + 1)}                                     # Initialize predecessor map for path         | N times
    repetitions += N                                                                # Count N parent initializations              | 1 time

    distances[S] = 0                                                                # Set distance from source S to itself as 0   | 1 time
    repetitions += 1                                                                # Count source distance assignment            | 1 time
    pq = [(0, S)]                                                                   # Initialize min-heap with (0, S)             | 1 time
    repetitions += 1                                                                # Count heap initialization                   | 1 time
    max_heap_size = 1                                                               # Track maximum size reached by min-heap      | 1 time

    if trace:                                                                       # Check if step-by-step trace output is on    | 1 time
        print(f"\n--- Dijkstra Trace (N={N}, S={S}, D={D}) ---")                     # Print trace table header                    | <= 1 time

    while pq:                                                                       # Loop until min-heap becomes empty           | <= E + 1 times
        repetitions += 1                                                            # Count each while-loop condition check       | <= E + 1 times
        current_dist, u = heapq.heappop(pq)                                         # Pop node u with smallest tentative dist     | <= E times

        if current_dist > distances[u]:                                             # Ignore outdated heap entry if worse         | <= E times
            continue                                                                # Skip relaxation for stale entry             | <= E - N times

        if trace:                                                                   # Print popped node details if tracing        | <= N times
            print(f"Popped: (dist={current_dist}, node={u}) | Heap: {pq}")          # Display current step state                  | <= N times

        if u == D:                                                                  # Stop early once destination D is finalized  | <= N times
            break                                                                   # Exit main loop since shortest path is found | <= 1 time

        for v, weight in adj[u]:                                                    # Iterate over outgoing edges of node u       | <= E times
            repetitions += 1                                                        # Count each edge relaxation check            | <= E times
            distance = current_dist + weight                                        # Calculate candidate distance to neighbor v  | <= E times
            if distance < distances[v]:                                             # Check if candidate path improves dist[v]    | <= E times
                distances[v] = distance                                             # Update shortest known distance to v         | <= E times
                parent[v] = u                                                       # Record u as predecessor of v                | <= E times
                heapq.heappush(pq, (distance, v))                                   # Push updated (distance, v) into min-heap    | <= E times
                repetitions += 1                                                    # Count heap push operation                   | <= E times
                if len(pq) > max_heap_size:                                         # Check if current heap exceeds max recorded  | <= E times
                    max_heap_size = len(pq)                                         # Update peak heap size                       | <= E times

    path = []                                                                       # Initialize list to reconstruct shortest path| 1 time
    curr = D                                                                        # Start backtracking from destination D       | 1 time
    while curr is not None:                                                         # Follow parent pointers back to source S     | <= N times
        repetitions += 1                                                            # Count each backtracking step                | <= N times
        path.append(curr)                                                           # Append visited node to path list            | <= N times
        curr = parent[curr]                                                         # Move to predecessor of current node         | <= N times
    path.reverse()                                                                  # Reverse path list to order from S to D      | 1 time
    repetitions += len(path)                                                        # Count reversal operations                   | 1 time

    if distances[D] == float('inf'):                                                # Check if destination D is unreachable       | 1 time
        return [], float('inf'), repetitions, max_heap_size                         # Return empty path and infinity if isolated  | <= 1 time

    return path, distances[D], repetitions, max_heap_size                           # Return path, cost, total reps, max heap     | 1 time