# def solution(arr, divisor):
#     answer = [i for i in arr if i % divisor == 0]
#     if(answer):
#         answer.sort()
#         return answer
#     else:
#         return [-1]

def solution(arr, divisor):
    answer = sorted([i for i in arr if i % divisor == 0])
    return answer if answer else [-1]

print(solution(arr=[2, 36, 1, 3], divisor=1))