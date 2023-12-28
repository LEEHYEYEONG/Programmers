def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i)*(food[i] // 2)
    answer += '0' + answer[::-1]
    return answer

def solution(food):
    answer = ''
    for i, n in enumerate(food[1:]):
        answer += str(i+1)*(n // 2)
    answer += '0' + answer[::-1]
    return answer

print(solution([1, 7, 1, 2]))