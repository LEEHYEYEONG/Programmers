def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    answer.reverse()
    return answer

# def solution(n):
#     return list(map(int, reversed(str(n))))

# def solution(n):
#     return [int(i) for i in str(n)][::-1]