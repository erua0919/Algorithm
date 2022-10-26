class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        preS, end = 0, {0: -1}

        for i, num in enumerate(nums):
            preS += num
            if k != 0:
                preS %= k 
            if preS in end: # keep the least index
                if i - end[preS] > 1:
                    return True
            else: 
                end[preS] = i 

        return False
        