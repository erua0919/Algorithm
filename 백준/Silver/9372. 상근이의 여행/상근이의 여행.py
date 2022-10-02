import sys
T = int(input())

for tc in range(T):    
    N,M = map(int,input().split())# N 국가 M 비행기 종류
    board = [] 
    for q in range(M):
        board.append(sys.stdin.readline().split()) 
    print(N-1)