def solution(a, b):
    answer = 0
    if a==b:
        answer=a
    elif a>b:
        c=0
        c=a
        a=b
        b=c
        for i in range(a,b+1):
            answer+=i
    else:
        for i in range(a,b+1):
            answer+=i
            
    return answer