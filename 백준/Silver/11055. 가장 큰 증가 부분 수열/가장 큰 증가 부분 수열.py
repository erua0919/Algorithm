n = int(input())
llist = list(map(int, input().split()))

dp = [x for x in llist]

for i in range(n):
    for j in range(i):
        if llist[i] > llist[j]:
            dp[i] = max(dp[i], dp[j] + llist[i])
print(max(dp))