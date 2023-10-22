def solution(n):
    ans = 1
    distance = 1


    while True:
        if(n - distance * 2 > 0):
            #n -= distance * 2
            distance *= 2
        elif(n - distance * 2 <= 0):
            #distance += n - distance
            ans += n - distance 
            distance += n - distance
            break

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return ans

print(solution(5000))