def knapsack(W, wt, val ,n):
    dp = [[0]*(W+1) for i in range(n+1)]
    for i in range(1,n+1):
        for w in range(0,W+1):
            if wt[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                a = dp[i-1][w]
                b = val[i-1] + dp[i-1][w-wt[i-1]]
                dp[i][w] = max(a,b)
    return dp[n][W]
# Example
val = [6, 10, 14, 4]
wt  = [2,  3,  4, 1]
W   = 6
n   = len(val)
print(knapsack(W, wt, val, n))   # Output: 20