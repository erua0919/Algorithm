class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        answer = False
        if "".join(word1) == "".join(word2):
            answer = True
            
        return answer