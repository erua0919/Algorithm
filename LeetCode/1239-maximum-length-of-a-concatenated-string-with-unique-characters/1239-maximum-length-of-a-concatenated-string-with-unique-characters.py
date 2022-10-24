class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        res = []
        for s in arr:
            # s 不包括重复
            if not len(set(s)) == len(s):
                continue
            tmpres = []
            for r in res:
                # 加入s
                if len(set(s).union(set(r))) == len(s)+len(r):
                    tmpres.append(s+r)
            res += tmpres
            res.append(s)
        # print(res)
        maxlen = 0
        for s in res:
            maxlen = max(maxlen, len(s))
        return maxlen