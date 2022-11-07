class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        for i in range(len(s)):
            if s[i]=='9':
                num = max(int(s[:i]+'6'+s[i+1:]), num)
            else:
                num = max(int(s[:i]+'9'+s[i+1:]), num)
        return num
