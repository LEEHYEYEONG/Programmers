# def solution(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
    
#     return solution(n-1) + solution(n-2)

def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    array = [0]*(n+1)
    array[0] = 0
    array[1] = 1
    
    for i in range(2, n+1):
        if array[i]:
            continue
        else:
            array[i] = array[i-1]+array[i-2]
    
    return array[-1] % 1234567

def solution(num):
    answer=[0,1]
    for i in range(2,num+1):
        answer.append(answer[i-1]+answer[i-2])
    return answer[-1] % 1234567

def solution(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a+b
    return a % 1234567

print(solution(0))
print(solution(5))