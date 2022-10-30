class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        if k >= M + N - 3:
            return M + N - 2

        DIRS = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        def isValid(i, j):
            return i >= 0 and i < M and j >= 0 and j < N

        # dp[i][j][k]: min steps to reach grid[i][j] with k obstacles available to remove
        dp = [[[M * N for k in range(k+1)] for _ in range(N)] for _ in range(M)]
        dp[0][0][k] = 0

        # [[x coordinate, y coordinate], # of obstacles left can remove]
        dq = collections.deque([[0, 0, k]])
        while dq:
            [x, y, remain] = dq.popleft()
            if x == M - 1 and y == N - 1:
                return dp[x][y][remain]
            for [dx, dy] in DIRS:
                nx, ny = x + dx, y + dy
                if not isValid(nx, ny):
                    continue
                left = remain - grid[nx][ny]
                if left >= 0 and dp[x][y][remain] + 1 < dp[nx][ny][left]:
                    dp[nx][ny][left] = dp[x][y][remain] + 1
                    dq.append([nx, ny, left])
        return -1
        