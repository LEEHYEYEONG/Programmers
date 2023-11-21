answer = 0
def solution(num):
    global answer
    if(num == 1):
        return 0
    elif(num % 2 == 0):
        num //= 2
        answer += 1
        if(num == 1):
            return answer
        else:
            solution(num)
    elif(num % 2 != 0):
        num = num * 3 + 1
        answer += 1
        solution(num)

    if(answer >= 500):
        return -1
    
    return answer
