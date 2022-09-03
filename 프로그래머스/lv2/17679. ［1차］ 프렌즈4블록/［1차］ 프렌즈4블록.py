def solution(m, n, board):
    import copy
    a=[list(board[i]) for i in range(m)]   
    while True:
        b=copy.deepcopy(a)   
        for i in range(m-1):
            for j in range(n-1):
                if a[i][j].upper()==a[i][j].upper()== \
                a[i][j+1].upper()==a[i+1][j].upper()==a[i+1][j+1].upper():
                    a[i][j] = a[i][j].lower()
                    a[i][j+1] = a[i][j+1].lower() 
                    a[i+1][j] = a[i+1][j].lower()
                    a[i+1][j+1] = a[i+1][j+1].lower()
        while True:
            c=copy.deepcopy(a)
            for i in range(m-1):
                for j in range(n):
                    if a[i+1][j]==a[i+1][j].lower():
                        a[i+1][j]=a[i][j]
                        a[i][j]=' '
            if a==c:
                break
        if a==b:
            break      
    answer=0
    for n, p in enumerate(a):
        b = ''.join(p)
        answer += b.count(' ')  
    return answer