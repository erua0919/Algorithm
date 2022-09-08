def solution(s):
    n = str(s)
    if len(n) % 2 == 0:
        return n[len(n)//2-1]+n[len(n)//2]
    else:
        return n[len(n)//2]