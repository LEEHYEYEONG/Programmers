def solution(left, right):
    divisor_list = [i if len([j for j in range(1, i+1) if i % j == 0]) % 2 == 0 else -i for i in range(left, right+1)]
    return sum(divisor_list)

print(solution(24, 27))