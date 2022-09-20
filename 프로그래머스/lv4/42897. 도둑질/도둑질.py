def solution(money):
    answer = 0
    dp = [0 for _ in range(len(money))]
    dp[0] = money[0]
    dp[1] = money[0]
    
    for i in range(2, len(money)-1):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    answer = max(dp)
    
    dp[0] = 0
    dp[1] = money[1]    
    for i in range(2, len(money)):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    if answer < max(dp):
        answer = max(dp)
    return answer