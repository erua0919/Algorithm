class Solution:
    def __init__(self):
        self.start = 0
        self.end = 0
        self.ans = 0
        self.p = []
    
    def maxProfit(self, k, prices):
        i = 1
        if len(prices) <= 1:
            return 0
        while i < len(prices):
            self.p.append(prices[i] - prices[i-1])
            i += 1
        if k >= len(self.p):
            return sum([x for x in self.p if x > 0])
        j = 0
        while j < k:
            ret = self.getProfit()
            if ret == 0:
                return self.ans
            self.ans += ret
            self.updatePrice()
            j += 1
        return self.ans

    def getProfit(self):
        s, tmpS = 0, 0
        tmpStart = 0
        for i in range(0 ,len(self.p)):
            tmpS += self.p[i]
            if tmpS <= 0:
                tmpS = 0
                tmpStart = i + 1
            else:
                if tmpS > s:
                    self.start = tmpStart
                    self.end = i + 1
                    s = tmpS
        return s

    def updatePrice(self):
        for i in range(self.start, self.end):
            self.p[i] *= -1