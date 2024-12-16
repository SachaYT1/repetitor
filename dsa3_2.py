def solve(cores, tasks, estimates):
    dp = [[float('inf')] * (tasks + 1) for _ in range(cores + 1)]

    for i in range(cores + 1):
        dp[i][0] = 0

    for i in range(1, cores + 1):
        for j in range(1, tasks + 1):
            dp[i][j] = float('inf')
            for k in range(1, j+1):
                dp[i][j] = min(dp[i][j], estimates[j-1][k-1] + dp[i-1][j-k])

    return dp[cores][tasks]

# Test the solve function
if __name__ == "__main__":
    estimates = [
        [500, 500, 500],
        [12, 13, 15],
        [10.5, 10, 11],
        [9, 8, 7.5],
        [7, 7, 4.5],
        [4.5, 5, 2]
    ]
    result = solve(5, 3, estimates)
    print("Minimum cost:", result)
