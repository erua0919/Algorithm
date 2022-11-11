class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:       
        
        llist = list(set(nums))
        llist.sort()
        for i in range(len(llist)):
            nums[i] = llist[i]
            
        return len(llist) 