from functools import lru_cache
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        N, M = len(nums), len(multipliers)
        @functools.lru_cache(2000)
        def dp(left: int, right: int) -> int:
            i = N - (right - left + 1)
            if i == M:
                return 0
            if left == right:
                return nums[left] * multipliers[i]
            return max(
                nums[left] * multipliers[i] + dp(left + 1, right),
                nums[right] * multipliers[i] + dp(left, right - 1),
            )
        return dp(0, N - 1)
        