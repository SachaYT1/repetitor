from pprint import pprint
def solve(C, A, E):
    # Create a DP table initialized with appropriate values
    dp = [[float('inf')] * (A + 1) for _ in range(C + 1)]

    # Initialize the base cases
    for i in range(C + 1):
        dp[i][0] = 0

    # Perform DP computation
    for i in range(1, C + 1):
        for j in range(1, A + 1):
            for k in range(1, i + 1):
                dp[i][j] = min(dp[i][j], E[k][j - 1] + dp[i - k][j - 1])

    # Return the result
    pprint(dp)
    # for i in range(1, C + 1):
    #     for j in range(1, A + 1):
    #         print(dp[i][j], end=' ')
    #     print()
    return dp[C][A]


# Test the minCost function
if __name__ == "__main__":
    E = [
        [500, 500, 500],
        [12, 13, 15],
        [10.5, 10, 11],
        [9, 8, 7.5],
        [7, 7, 4.5],
        [4.5, 5, 2]
    ]
    A = 5  # number of tasks
    C = 3  # number of cores
    result = solve(A, C, E)
    print("Minimum cost:", result)
