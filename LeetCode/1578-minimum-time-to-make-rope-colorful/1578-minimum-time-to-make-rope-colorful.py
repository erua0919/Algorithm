class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i = 0
        res = 0
        colors = list(colors)
        while i < len(colors):
            j = i + 1
            if j < len(colors) and colors[j] == colors[i]:
                while j < len(colors) and colors[j] == colors[i]:
                    j += 1
                for idx in range(i, j):
                    res += neededTime[idx]
                res -= max(neededTime[i:j])
                i = j
            else:
                i += 1
        return res