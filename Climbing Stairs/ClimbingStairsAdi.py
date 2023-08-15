class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n):
            dp[i][i]=1
            dp[i][i+1]=1
        if n==1:
            return dp[0][1]
        for i in range(2,n+1):
            for j in range(n-i,-1,-1):
                dp[j][j+i]=dp[j][j+i-1]+dp[j][j+i-2]
        return dp[0][n]
