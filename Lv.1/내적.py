def solution(a, b):
    answer = sum([a[i]*b[i] for i in range(len(a))])
    return answer

print(solution(a=[-1,0,1], b=[1,0,-1]))