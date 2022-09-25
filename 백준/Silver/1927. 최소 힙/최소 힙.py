from sys import stdin

input = stdin.readline
class MinHeap:

    def __init__(self):
        self.que = [0]

    def insert(self, x):
        self.que.append(x)
        idx = len(self.que) - 1  # 현재 인덱스
        while 1 < idx:
            if self.que[idx] < self.que[idx // 2]:  # 부모가 더 크면 swap
                self.swap(idx, idx // 2)
                idx = idx // 2
            else:  
                break

    def delete(self):
        if len(self.que) == 1:
            return 0
        self.swap(1, -1)
        _min = self.que.pop()
        self.sort()
        return _min
    def swap(self, i1, i2):
        self.que[i1], self.que[i2] = self.que[i2], self.que[i1]

    def sort(self):
        _idx = 1

        while len(self.que) > 1:
            _next = _idx
            if _idx * 2 < len(self.que) and self.que[_idx * 2] < self.que[_next]:
                _next = _idx * 2

            if _idx * 2 + 1 < len(self.que) and self.que[_idx * 2 + 1] < self.que[_next]:
                _next = _idx * 2 + 1

            if _next != _idx :
                self.swap(_idx, _next)
                _idx = _next
            else:
                break
if __name__ == "__main__":
    N = int(input())
    pq = MinHeap()
    for _ in range(N):
        x = int(input())
        if x == 0:
            print(pq.delete())
        else:
            pq.insert(x)