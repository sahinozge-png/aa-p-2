import math                                                                         # Import math for log2 theoretical calculation| 1 time
import matplotlib.pyplot as plt                                                     # Import matplotlib for benchmark plotting    | 1 time
from dijkstra import dijkstra                                                       # Import Dijkstra's algorithm                 | 1 time
from astar import astar                                                             # Import A* search algorithm                  | 1 time

def run_interactive(choice):                                                        # Run interactive mode based on user choice   | 1 time
    print("\n--- Interactive Mode (N < 20) ---")                                    # Print interactive header                    | 1 time
    try:                                                                            # Handle non-integer or invalid range inputs  | 1 time
        N = int(input("Enter number of cities N (< 20): "))                         # Read number of cities N from user           | 1 time
        if N >= 20 or N < 1:                                                        # Enforce constraint 1 <= N < 20              | 1 time
            print("Error: N must be between 1 and 19.")                             # Display range error message                 | <= 1 time
            return                                                                  # Exit interactive mode on invalid N          | <= 1 time

        S = int(input(f"Enter source city S (1 to {N}): "))                         # Read source city S                          | 1 time
        D = int(input(f"Enter destination city D (1 to {N}): "))                    # Read destination city D                     | 1 time

        if choice in ('1', '3'):                                                    # Run Dijkstra if option 1 or 3 is selected   | 1 time
            path_d, cost_d, reps_d, max_pq = dijkstra(N, S, D, trace=(choice == '1')) # Execute Dijkstra (trace if solo)          | <= 1 time
            print(f"\n[Dijkstra] Shortest Path    : {path_d}")                      # Print Dijkstra shortest path                | <= 1 time
            print(f"[Dijkstra] Total Cost       : {cost_d}")                        # Print Dijkstra total cost                   | <= 1 time
            print(f"[Dijkstra] Total Repetitions: {reps_d}")                        # Print Dijkstra repetition count             | <= 1 time
            print(f"[Dijkstra] Max Heap Size    : {max_pq}")                        # Print Dijkstra peak heap size               | <= 1 time

        if choice in ('2', '3'):                                                    # Run A* if option 2 or 3 is selected         | 1 time
            path_a, cost_a, reps_a, exp_a = astar(N, S, D)                          # Execute A* search algorithm                 | <= 1 time
            print(f"\n[A* Search] Shortest Path   : {path_a}")                      # Print A* shortest path                      | <= 1 time
            print(f"[A* Search] Total Cost      : {cost_a}")                        # Print A* total cost                         | <= 1 time
            print(f"[A* Search] Total Repetitions: {reps_a}")                       # Print A* repetition count                   | <= 1 time
            print(f"[A* Search] Nodes Expanded  : {exp_a}")                         # Print number of nodes expanded by A*        | <= 1 time

    except ValueError as e:                                                         # Catch invalid S/D or non-numeric input      | <= 1 time
        print(f"Input Error: {e}")                                                  # Print descriptive error message             | <= 1 time

def run_benchmark(choice):                                                          # Run benchmark scaling experiment (S=1, D=N) | 1 time
    print("\n--- Benchmark Mode (S=1, D=N) ---")                                    # Print benchmark mode header                 | 1 time
    test_sizes = [10, 50, 100, 200, 500, 1000, 2000]                                # Define required test sizes N                | 1 time
    d_reps, a_reps, theo_reps = [], [], []                                          # Initialize lists to store benchmark results | 1 time

    if choice == '1':                                                               # Header for Dijkstra-only benchmark          | 1 time
        print(f"{'N':<6} | {'E=6N-12':<8} | {'Dijkstra Reps':<14} | {'Reps/N':<8} | {'Max Heap':<8}") # Print Dijkstra table header    | <= 1 time
        print("-" * 56)                                                             # Print divider line                          | <= 1 time
    elif choice == '2':                                                             # Header for A*-only benchmark                | 1 time
        print(f"{'N':<6} | {'E=6N-12':<8} | {'A* Reps':<14} | {'Reps/N':<8} | {'Expanded':<8}") # Print A* table header          | <= 1 time
        print("-" * 56)                                                             # Print divider line                          | <= 1 time
    else:                                                                           # Header for combined comparison benchmark    | 1 time
        print(f"{'N':<6} | {'Dijkstra Reps':<14} | {'A* Reps':<14} | {'Max Heap':<9} | {'A* Expanded':<11}") # Print combined header   | <= 1 time
        print("-" * 66)                                                             # Print divider line                          | <= 1 time

    for N in test_sizes:                                                            # Loop over all 7 input sizes N               | 7 times
        E = 6 * N - 12                                                              # Calculate exact edge count E = 6N - 12      | 7 times
        raw_theo = (N + E) * math.log2(N)                                           # Compute theoretical O((V+E) log V) term     | 7 times
        theo_reps.append(raw_theo)                                                  # Store theoretical value                     | 7 times

        if choice in ('1', '3'):                                                    # Measure Dijkstra if option 1 or 3           | 7 times
            _, _, rd, max_pq = dijkstra(N, 1, N, trace=False)                       # Run Dijkstra for S=1, D=N                   | <= 7 times
            d_reps.append(rd)                                                       # Record Dijkstra repetitions                 | <= 7 times

        if choice in ('2', '3'):                                                    # Measure A* if option 2 or 3                 | 7 times
            _, _, ra, exp_a = astar(N, 1, N)                                        # Run A* for S=1, D=N                         | <= 7 times
            a_reps.append(ra)                                                       # Record A* repetitions                       | <= 7 times

        if choice == '1':                                                           # Print Dijkstra row                          | 7 times
            print(f"{N:<6} | {E:<8} | {rd:<14} | {rd/N:<8.2f} | {max_pq:<8}")       # Format Dijkstra benchmark output            | <= 7 times
        elif choice == '2':                                                         # Print A* row                                | 7 times
            print(f"{N:<6} | {E:<8} | {ra:<14} | {ra/N:<8.2f} | {exp_a:<8}")        # Format A* benchmark output                  | <= 7 times
        else:                                                                       # Print combined comparison row               | 7 times
            print(f"{N:<6} | {rd:<14} | {ra:<14} | {max_pq:<9} | {exp_a:<11}")      # Format combined comparison output           | <= 7 times

    plt.figure(figsize=(9, 5))                                                      # Create matplotlib figure                    | 1 time
    ref_reps = d_reps if choice in ('1', '3') else a_reps                           # Select reference series for theoretical fit | 1 time
    scale = ref_reps[-1] / theo_reps[-1]                                            # Compute scaling factor for theoretical plot | 1 time
    scaled_theo = [t * scale for t in theo_reps]                                    # Scale theoretical curve                     | 7 times

    if choice in ('1', '3'):                                                        # Plot Dijkstra curve if selected             | 1 time
        plt.plot(test_sizes, d_reps, 'o-', label='Dijkstra (Actual Reps)', linewidth=2) # Plot Dijkstra measured repetitions      | <= 1 time
    if choice in ('2', '3'):                                                        # Plot A* curve if selected                   | 1 time
        plt.plot(test_sizes, a_reps, '^-', label='A* Search (Actual Reps)', linewidth=2) # Plot A* measured repetitions          | <= 1 time

    plt.plot(test_sizes, scaled_theo, 's--', label='Theoretical O((V+E) log V) [Scaled]', linewidth=2) # Plot theoretical curve | 1 time
    plt.title("Shortest Path Algorithms: Actual Repetitions vs. Theoretical Complexity") # Set graph title                        | 1 time
    plt.xlabel("Number of Cities (N)")                                              # Set X-axis label                            | 1 time
    plt.ylabel("Operations / Repetitions")                                          # Set Y-axis label                            | 1 time
    plt.legend()                                                                    # Show plot legend                            | 1 time
    plt.grid(True, linestyle=':', alpha=0.7)                                        # Add dashed gridlines                        | 1 time
    plt.tight_layout()                                                              # Optimize figure padding                     | 1 time
    plt.savefig("benchmark_comparison.png", dpi=300)                                # Save plot image for report                  | 1 time
    print("\nSaved benchmark plot to 'benchmark_comparison.png'.")                  # Confirm plot saved                          | 1 time
    plt.show()                                                                      # Render plot window                          | 1 time

def main():                                                                         # Main menu controller                        | 1 time
    print("=========================================")                              # Print top menu border                       | 1 time
    print("  COMP 303 Project 2 - Shortest Path     ")                              # Print program title                         | 1 time
    print("=========================================")                              # Print bottom menu border                    | 1 time
    print("1. Dijkstra's Algorithm")                                                # Menu option 1                               | 1 time
    print("2. A* Search Algorithm")                                                 # Menu option 2                               | 1 time
    print("3. Compare Both Algorithms")                                             # Menu option 3                               | 1 time

    choice = input("\nSelect an option (1, 2, or 3): ").strip()                     # Read user menu selection                    | 1 time
    if choice not in ('1', '2', '3'):                                               # Validate menu selection                     | 1 time
        print("Invalid selection. Please choose 1, 2, or 3.")                       # Display invalid choice message              | <= 1 time
        return                                                                      # Exit on invalid choice                      | <= 1 time

    run_interactive(choice)                                                         # Run interactive test for chosen option      | 1 time
    run_benchmark(choice)                                                           # Run benchmark & plot for chosen option      | 1 time

if __name__ == "__main__":                                                          # Python entry point check                    | 1 time
    main()                                                                          # Invoke main menu function                   | 1 time