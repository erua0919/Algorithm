class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        speeds = 0
        ans = 0
        q = []
        for e, s in sorted(zip(efficiency, speed), reverse=True):
          if len(q) >= k:
            speeds -= heapq.heappop(q)
          speeds += s
          heapq.heappush(q, s)
          ans = max(ans, speeds * e)
        return ans % (10**9 + 7)
        