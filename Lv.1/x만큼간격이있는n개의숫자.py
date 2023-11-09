def solution(x, n):
    answer = []
    init_x = x
    for _ in range(n):
        answer.append(x)
        x += init_x
    return answer

# def solution(x, n):
#     answer=[]
#     for i in range(n):
#         answer.append((i+1)*x)
#     return answer