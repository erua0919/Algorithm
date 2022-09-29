class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        i, j = 0, len(arr) - k
        while i < j:
            mid = (i & j) + ((i^j)>> 1)
            if x - arr[mid] > arr[mid + k] - x: # arr is sorted
                i = mid + 1
            else:
                j = mid

        return arr[i:i+k]