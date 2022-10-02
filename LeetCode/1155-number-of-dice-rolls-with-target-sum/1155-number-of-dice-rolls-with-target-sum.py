class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10**9+7
        dp = [[0]*(target + 1) for _ in range(d + 1)]#dp[i][j] i: ith dices j: temp target
        dp[0][0] = 1
        if target < 1 or target > d*f: return 0
        for i in range(1, d + 1):
            for j in range(1, f + 1):
                for k in range(j, target + 1):
                    dp[i][k] = (dp[i][k] + dp[i-1][k-j]) % mod
        return dp[-1][-1]
        