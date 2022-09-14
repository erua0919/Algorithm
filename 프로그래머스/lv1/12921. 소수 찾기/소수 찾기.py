import math
def solution(n):
    arr = set(range(2, n+1))
    i = 2
    while i < int(math.sqrt(n) + 1):
        arr -= set([i*k for k in range(2, n//i + 1)])
        i += 1

    return len(arr)