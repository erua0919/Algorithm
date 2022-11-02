class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        wordset = set(bank)
        #print(wordset)
        wordset.add(start)
        meet = set()
        if end not in wordset:return -1
        res = 0
        que = collections.deque()
        que.append(start)
        letters = 'ACTG'
        while que:
            size = len(que)
            for i in range(size):
                curword = que.popleft()
                meet.add(curword)
                for j in range(8):
                    for c in letters:
                        curnewword = curword[:j] + c + curword[j+1:]
                        if curnewword not in wordset:
                            continue
                        if curnewword not in meet:
                            if curnewword == end:return res+1
                            else:que.append(curnewword)
            res += 1
        return -1