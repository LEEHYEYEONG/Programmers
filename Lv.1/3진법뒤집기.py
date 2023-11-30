def solution(n):
    seven_reverse = []
    while n != 0:
        seven_reverse.append(str(n % 3))
        n //= 3
    
    return int(''.join(seven_reverse), 3)

def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

print(solution(125))