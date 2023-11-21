def solution(a, b):
    max_num, min_num = max(a, b), min(a, b)
    answer = sum([i for i in range(min_num, max_num+1)])
    return answer

# def solution(a, b):
#     return (abs(a-b)+1)*(a+b)//2
