def solution(N, number):
    dp = [[] for _ in range(9)]

    for i in range(1, 9):
        # N이 i번 반복되는 경우 
        dp[i].append(int(str(N)*(i)))
        for j in range(1, i):
            # N이 j번 쓰인 경우의 수와 N이 i-j번 쓰인 경우의 사칙연산
            for x in dp[j]:
                for y in dp[i-j]:
                    dp[i].append(x+y)
                    dp[i].append(x-y)
                    dp[i].append(x*y)
                    if y != 0:
                        dp[i].append(x//y)
        
        if number in dp[i]:
            return i

    return -1