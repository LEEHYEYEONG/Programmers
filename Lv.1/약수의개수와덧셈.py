# def solution(left, right):
#     divisor_list = [i if len([j for j in range(1, i+1) if i % j == 0]) % 2 == 0 else -i for i in range(left, right+1)]
#     return sum(divisor_list)

# 제곱수의 약수의 개수가 홀수 임을 이용한 풀이
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

print(solution(24, 27))