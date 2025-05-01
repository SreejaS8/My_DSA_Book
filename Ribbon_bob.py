def solve(N):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0  # Base case: No ribbon needed for size 0
    
    # Iterate over all required sizes
    for i in range(1, N + 1):
        # Try cutting ribbons of size j (Bob has ribbons up to N+1)
        for j in range(1, N + 2):
            if i >= j:
                dp[i] = min(dp[i], dp[i - j] + 1)
    
    print(dp[N])

# Test Cases
T = int(input())  # Number of test cases
for _ in range(T):
    N = int(input())
    solve(N)