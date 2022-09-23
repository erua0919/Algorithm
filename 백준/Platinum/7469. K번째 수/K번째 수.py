from math import ceil, log2
import sys;rl = sys.stdin.readline
n,m = map(int,rl().split())
An = list(map(int,rl().split()))
leafLevel = int(log2(n))+1

def merge(leftList:list,rightList:list):
    rtnList = []
    leftIter = 0
    rightIter = 0
    while leftIter < len(leftList) and rightIter < len(rightList):
        if leftList[leftIter] < rightList[rightIter]:
            rtnList.append(leftList[leftIter])
            leftIter+=1
        else:
            rtnList.append(rightList[rightIter])
            rightIter+=1
    rtnList+=leftList[leftIter:]
    rtnList+=rightList[rightIter:]
    return rtnList

def init():
    for i in range(2**leafLevel):
        MST[(2**leafLevel)+i][0] = MST[(2**leafLevel)+i][1] = i+1
    for i in range(n):
        MST[(2**leafLevel)+i][2].append(An[i])
    level = leafLevel-1
    while level>=0:
        for i in range(2**level,2**(level+1)):
            MST[i][0] = MST[i*2][0]
            MST[i][1] = MST[i*2+1][1]
            MST[i][2] = merge(MST[i*2][2],MST[i*2+1][2])
        level-=1
MST = [[0,0,[]] for _ in range(2**(leafLevel+1))]
#MST의 노드는 [구간시작,구간끝,[자식노드 머지한 리스트]] 형태.
MST[0] = None
init()

def upperBound(x,nodeIndex):
    left = 0
    right = len(MST[nodeIndex][2])-1
    mid = 0
    while left<right:
        if MST[nodeIndex][2][mid]<=x:
            left = mid + 1
        else:
            right = mid
        mid = (left+right)//2
        if mid == right:
            if MST[nodeIndex][2][mid] <= x:
                return len(MST[nodeIndex][2])
            else:
                return right
    if MST[nodeIndex][2][left] > x:
        return 0
    return left + 1

def query(x,start,end,nodeIndex): 
    left = MST[nodeIndex][0]
    right = MST[nodeIndex][1]
    if left > end or right < start:
        return 0
    elif start<=left and right<=end:
        return upperBound(x,nodeIndex)
    return query(x,start,end,nodeIndex*2)+query(x,start,end,nodeIndex*2+1)

for _ in range(m):
    i,j,k = map(int,rl().split())
    start = -(10**9)
    end = 10**9
    while start<=end:
        mid = (start+end)//2
        result = query(mid,i,j,1)
        if result<k:
            start = mid + 1
        else:
            end = mid - 1
    print(start)