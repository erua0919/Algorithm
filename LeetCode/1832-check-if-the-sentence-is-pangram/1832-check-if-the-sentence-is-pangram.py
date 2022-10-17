from collections import Counter
class Solution:
    def checkIfPangram(self, sentence):
        if len(sentence)<26:
            return False
        if len(Counter(sentence).keys())<26:
            return False
        else:
            return True