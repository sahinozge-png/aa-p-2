from dijkstra import dijkstra

def run_interactive():
    print("--- Interactive Mode (N < 20) ---")
    N = int(input("Enter number of cities N (< 20): "))
    if N >= 20 or N < 1:
        print("Error: N must be between 1 and 19.")
        return
        
    S = int(input(f"Enter source city S (1 to {N}): "))
    D = int(input(f"Enter destination city D (1 to {N}): "))
    
    path_d, cost_d, reps_d = dijkstra(N, S, D)
    print(f"\n[Dijkstra] Shortest Path: {path_d}")
    print(f"[Dijkstra] Total Cost: {cost_d}")
    print(f"[Dijkstra] Total Repetitions: {reps_d}")

def run_benchmark():
    print("\n--- Benchmark Mode (S=1, D=N) ---")
    test_sizes = [10, 50, 100, 200, 500, 1000, 2000]
    print(f"{'N':<8} | {'Dijkstra Reps':<15}")
    print("-" * 28)
    for N in test_sizes:
        _, _, reps_d = dijkstra(N, 1, N)
        print(f"{N:<8} | {reps_d:<15}")

if __name__ == "__main__":
    run_interactive()
    run_benchmark()