class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        forward = []
        backward = []
        
        forward.append(nums[0])
        
        for i in range(1, len(nums)):
            num = nums[i]
            if num < forward[i - 1]:
                forward.append(num)
            else:
                forward.append(forward[i - 1])
                
        backward.append(nums[len(nums) - 1])
        for i in range(1, len(nums)):
            num = nums[len(nums) - i - 1]            
            if num > backward[i - 1]:
                backward.append(num)
            else:
                backward.append(backward[i - 1])                

        backward.reverse()
        
        for i in range(0, len(nums)):
            num = nums[i]
            if backward[i] > num > forward[i]:
                return True      
            
        return False