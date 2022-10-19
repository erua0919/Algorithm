from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        
        print(cnt.items())
        
        most_list = sorted(list(cnt.items()), key=lambda x: [-x[1], x[0]])
        
        print(most_list)
        
        answer = []
        
        for i in range(k):
            answer.append(most_list[i][0])
            
        return answer