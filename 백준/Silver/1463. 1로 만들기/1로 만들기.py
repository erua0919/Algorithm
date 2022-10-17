n = int(input())
dp = [0] * (n + 1)
for i in range(2, n+1):

    # 첫번째 방법 1을 빼줌
    dp[i] = dp[i-1] + 1

    # 3으로 나눌수 있으면 나눠서 최소값 비교
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    # 2로 나눌 수 있으면 나눠서 최소값 비교
    if i % 2 == 0:
        # 6 > 3 > 1로 가는 방법
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[n])