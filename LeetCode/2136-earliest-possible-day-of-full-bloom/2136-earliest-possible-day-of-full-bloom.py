class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        """
        :type plantTime: List[int]
        :type growTime: List[int]
        :rtype: int
        """

        res = 0
        now = 0
        for p, g in sorted(zip(plantTime, growTime), key=lambda d:d[1], reverse=True):
            now += p
            res = max(res, now + g)
        
        return res