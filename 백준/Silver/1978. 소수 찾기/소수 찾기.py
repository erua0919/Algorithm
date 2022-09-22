N=int(input())
arr=list(map(int,input().split()))

prime={}
cnt=0

for i in range(1,1001):
    prime[i]=True

prime[1]=False

for i in range(2,int(1000**0.5)+1):
    if prime[i]==True:
        for j in range(i+i,1001,i):
            prime[j]=False



for i in arr:
    if prime[i]==True:
        cnt+=1

print(cnt)