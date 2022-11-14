class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def find(set, x):
            if set[x] == -1:
                return x
            return find(set, set[x])

        def union(set, x, y):
            rx = find(set, x)
            ry = find(set, y)
            if rx != ry:
                set[rx] = ry
        
        N = len(stones)
        set = [-1] * N
        for i in range(N):
            for j in range(i + 1, N):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(set, i, j)

        res = N
        for i in range(N):
            if set[i] == -1:
                res -= 1
        return res